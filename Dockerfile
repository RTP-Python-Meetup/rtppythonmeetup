FROM python:3.8-alpine

RUN apk update && \
    apk upgrade && \
    pip install pipenv

ARG PROJECT=rtppythonmeetup
ARG PROJECT_DIR=/opt/$PROJECT

RUN adduser $PROJECT -D

RUN mkdir -p $PROJECT_DIR && \
    chown rtppythonmeetup:rtppythonmeetup $PROJECT_DIR

USER $PROJECT
WORKDIR $PROJECT_DIR
COPY Pipfile ./
RUN pipenv install

EXPOSE 8000
STOPSIGNAL SIGINT

