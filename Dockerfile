FROM python:3.3-alpine

# Timezone Europe/Brussels
ENV TZ=Europe/Brussels
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .

EXPOSE 5000
CMD python api.py
