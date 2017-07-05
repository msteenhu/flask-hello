FROM python:3.3-alpine


RUN apk add --update build-base libffi-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .

EXPOSE 5000
CMD python api.py
