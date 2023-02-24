# action-sharepoint-folder-upload

This action will upload the contents of a specified folder to a Sharepoint site.

## Inputs

| Input name            | Required  | Description                                                                               | Example                                                                |
|-----------------------| :-------: |-------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| `site_url`            | **Yes**   | The Sharepoint site url                                                                   | `https://swedwise-my.sharepoint.com/personal/henrik_blidh_swedwise_se` |
| `sharepoint_user`     | **Yes**   | The username to use for authentication                                                    | `bob.tester@funnypage.com`                                             |
| `sharepoint_password` | **Yes**   | The user's password </br> ***Use GitHub Actions Secrets to store sensible informations*** | `MyPassword123!`                                                       |
| `destination_folder`  | **Yes**   | The path relative to site where to upload a file                                          | `Documents/Upload`                   |
| `folder`              | **Yes**   | The path of the folder you want to upload                                                 | `${{ github.workspace }}/`                                     |


## Example usage 

This can be used for e.g. publishing static sites to a Sharepoint server.

```yml
name: 'Sharepoint Upload'

on:
  release:
    types: created

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
    
    - name: Clone your repo
      uses: actions/checkout@v3

    - name: Sharepoint upload file
      uses: swedwise/action-sharepoint-folder-upload@v1
      with:
        site_url: 'https://swedwise-my.sharepoint.com/personal/henrik_blidh_swedwise_se'
        sharepoint_user: ${{ secrets.USER }}
        sharepoint_password: ${{ secrets.PASS }}
        destination_folder: "Documents/Upload"
        folder: "./_build/StaticSite/"
```
