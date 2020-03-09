FROM python:3.8-alpine

RUN apk update && \
    apk upgrade && \
    pip install pipenv

ARG PROJECT=rtppythonmeetup
ARG PROJECT_DIR=/opt/$PROJECT

ARG UNAME=$PROJECT
ARG UID=1000

RUN adduser \
        --disabled-password \
        --gecos "" \
        --home "$PROJECT_DIR" \
        --no-create-home \
        --uid "$UID" \
        "$UNAME" && \
    mkdir -p $PROJECT_DIR && \
    chown $UNAME:$UNAME $PROJECT_DIR

USER $PROJECT
WORKDIR $PROJECT_DIR
COPY Pipfile ./
RUN pipenv install

EXPOSE 8000
STOPSIGNAL SIGINT

