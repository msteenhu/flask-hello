from flask import Flask, request, send_file
from flask_prometheus import monitor
app = Flask(__name__)
monitor(app, port=6001)

@app.route("/headers")
def hello():
    return "<xmp>Headers:\n{}Remote Address:\n{}</xmp>".format(request.headers, request.remote_addr)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/happy")
def phippy_happy():
    return send_file("phippy_happy.png", mimetype="image/png")

@app.route("/scared")
def phippy_unhappy():
    return send_file("phippy.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
