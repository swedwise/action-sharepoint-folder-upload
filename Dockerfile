# Container image that runs your code
FROM python:3.10-slim

# RUN apk add gcc --update   # cairo-dev pango-dev gdk-pixbuf-dev
RUN pip install shareplum

# Copies your code file from your action repository to the filesystem path `/` of the container
ADD . /app
RUN chmod -r /app 777

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/app/entrypoint.sh"]
