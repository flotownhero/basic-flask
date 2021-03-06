FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

COPY src/ /opt/

# RUN pip install flask 
RUN pip install -r /opt/requirements.txt

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080
