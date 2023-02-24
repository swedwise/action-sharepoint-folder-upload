# Container image that runs your code
FROM python:3.11-slim

# RUN apk add gcc --update   # cairo-dev pango-dev gdk-pixbuf-dev
RUN pip install shareplum

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY main.py /app/main.py

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["python /app/main.py"]
