FROM python:3.8
# FROM gitlab-registry.gs.mil/bluefactory/docker/python:3.10.0-2 

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
COPY src/ .

RUN pip3 install -r requirements.txt

# EXPOSE 5042

# run the app
CMD ["python3", "./app.py"]