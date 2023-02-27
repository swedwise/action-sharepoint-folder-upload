import os
from pathlib import Path
from urllib.parse import urlparse

from shareplum import Site, Office365
from shareplum.site import Version
from shareplum.folder import _Folder

SITE_URL = os.getenv("SITE_URL")
USER = os.getenv("USER")
PASS = os.getenv("PASS")
DESTINATION = os.getenv("DESTINATION")
FOLDER = os.getenv("FOLDER")


def gh_action_log(message, level="notice"):
    print(f"::{level} file={Path(__file__).name}::{message}", flush=True)


def upload_folder(local_folder: Path, destination: str, site: Site):
    """Upload the contents of a folder to Sharepoint."""
    sp_folder = site.Folder(destination)
    for path in Path(local_folder).glob("*"):
        if path.is_file():
            # Handle single file.
            upload_file(path, sp_folder)
        elif path.is_dir():
            if path.name in (".git", ".idea"):
                continue
            # Get path of new folder and create it
            new_destination = f"{destination}/{path.stem}"
            site.Folder(new_destination)
            gh_action_log(f"Created folder '{new_destination}'")
            # Now make recursive call to self with new folder
            upload_folder(path, new_destination, site)


def upload_file(file: Path, folder: _Folder):
    """Uploads a single file to a specified Sharepoint folder"""
    with file.open(mode="rb") as f:
        folder.upload_file(f.read(), file.name)
        gh_action_log(f"Uploaded file {folder.folder_name}/{file.name}")


def main():
    # First, get the auth url from the SITE_URL
    url_parts = urlparse(SITE_URL)
    # Get an auth cookie
    auth_cookie = Office365(
        f"{url_parts.scheme}://{url_parts.hostname}", username=USER, password=PASS
    ).GetCookies()
    # Create Site object and start uploading
    site = Site(SITE_URL, authcookie=auth_cookie, version=Version.v365)
    upload_folder(Path(FOLDER), DESTINATION, site)


if __name__ == "__main__":
    main()
