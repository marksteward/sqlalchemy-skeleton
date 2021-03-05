FROM ubuntu

RUN apt-get update && apt-get -y install python3 python3-pip python3-psycopg2 vim

RUN pip3 install sqlalchemy

WORKDIR /app

COPY main.py .

