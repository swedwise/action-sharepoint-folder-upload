# Container image that runs your code
FROM python:3.10-slim
RUN pip install shareplum
ADD . /app
RUN chmod 777 /app -R
ENTRYPOINT ["/app/entrypoint.sh"]