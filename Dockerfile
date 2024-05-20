FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python migrations
RUN python app.py


EXPOSE 5000
