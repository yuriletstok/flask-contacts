FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python-3.11

RUN pip install -r requirements.txt
RUN python migrations
RUN python app.py


EXPOSE 5000