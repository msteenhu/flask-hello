FROM python:3.3-alpine
RUN pip install flask flask-prometheus
COPY api.py api.py
COPY phippy.png phippy.png
COPY phippy_happy.png phippy_happy.png
EXPOSE 6000
CMD python api.py
