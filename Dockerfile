FROM ubuntu

RUN apt-get update && apt-get -y install python3 python3-pip vim

RUN pip3 install sqlalchemy

WORKDIR /root

COPY main.py .

