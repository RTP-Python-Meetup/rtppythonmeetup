FROM python:3.8-alpine

RUN apk update && \
    apk upgrade && \
    pip install pipenv

ARG PROJECT=rtppythonmeetup
ARG PROJECT_DIR=/opt/$PROJECT

ARG UNAME=$PROJECT
ARG UID=1000
ARG GID=1000

RUN addgroup -g ${GID} ${UNAME} && \
    adduser \
        --disabled-password \
        --gecos "" \
        --uid "$UID" \
        -G ${UNAME} \
        "$UNAME" && \
    mkdir -p $PROJECT_DIR && \
    chown $UNAME:$UNAME $PROJECT_DIR

USER $PROJECT
WORKDIR $PROJECT_DIR
COPY Pipfile ./
RUN pipenv install

EXPOSE 8000
STOPSIGNAL SIGINT

