from flask import Flask, request, send_file
from flask_prometheus import monitor

import socket
import time

app = Flask(__name__)
monitor(app, port=6001)


@app.route("/")
def index():
    return "Hello world!"

@app.route("/host")
def ip():
    return socket.gethostname()

@app.route("/headers")
def hello():
    return "<xmp>Headers:\n{}Remote Address:\n{}</xmp>".format(request.headers, request.remote_addr)

@app.route("/cpuload")
def cpuload():
    till = time.time() + 20 # 20 seconds load
    while (time.time() < till):
        pr = 213123
        pr * pr
        pr = pr + 1
    return "Worked for 20s, now tired...", 200

@app.route("/happy")
def phippy_happy():
    return send_file("phippy_happy.png", mimetype="image/png")

@app.route("/scared")
def phippy_unhappy():
    return send_file("phippy.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
