FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Europe/Moscow
RUN apt-get -qqy update && pip install poetry && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /fitness
COPY pyproject.toml /fitness/

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . /fitness
WORKDIR /fitness

