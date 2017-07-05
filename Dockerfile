FROM python:3.3-alpine

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .

EXPOSE 5000
CMD python api.py
