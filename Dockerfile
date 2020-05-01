FROM python:3.8.2-slim-buster

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y build-essential python-dev python3-pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT []