FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install --yes git

COPY ./requirements.txt /nanoserver/requirements.txt
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install -r /nanoserver/requirements.txt

WORKDIR /nanoserver
COPY ./ .

ENTRYPOINT [ "/nanoserver/init-flask.sh" ]
