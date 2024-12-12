FROM python:3.13-slim

WORKDIR /app

COPY ./app /app
COPY ./payload.ps /app
COPY ./payload2.ps /app

RUN pip install --no-cache-dir flask

CMD ["python", "app.py"]

EXPOSE 80