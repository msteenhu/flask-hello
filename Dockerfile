FROM python:3.3-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /flask-hello

COPY . .

EXPOSE 5000
CMD python api.py
