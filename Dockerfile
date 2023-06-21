FROM python:3.8.13-alpine3.15
COPY . /app
WORKDIR /app
VOLUME /app/data
