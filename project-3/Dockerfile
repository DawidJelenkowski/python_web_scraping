# name:tag
FROM python:3.10

# set up working directory
WORKDIR /code

# packages to install
COPY ./requirements.txt requirements.txt


RUN yes | apt-get update
# clears cache and install requirements
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# specify what to copy
COPY ./requirements2.txt requirements2.txt
COPY ./extensions.txt extensions.txt

# run commands after starting the container
CMD ["python"]