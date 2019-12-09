#use python as base image
FROM python:3.7-slim

#use working directory /app
WORKDIR /app

#copy all the content of current directory to /app
ADD . /app

#install requirement packages
RUN pip install -r requirements.txt

#open port 5000
EXPOSE 5000

#set environment variable
ENV NAME OpentoAll

#run python program
CMD ["python","app.py"]
