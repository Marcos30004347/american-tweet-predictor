FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY ./app.py ./app.py

RUN pip3 install flask requests scikit-learn

CMD [ "python3", "-m" , "flask", "run", "--port=5022", "--host=0.0.0.0"]