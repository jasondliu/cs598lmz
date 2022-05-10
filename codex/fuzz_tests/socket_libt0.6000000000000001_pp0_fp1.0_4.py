import socket

from flask import Flask, request
import requests

app = Flask(__name__)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/service")
def service():
    return "Service 1"


@app.route("/service2")
def service2():
    return "Service 2"


@app.route("/service3")
def service3():
    return "Service 3"


@app.route("/service4")
def service4():
    return "Service 4"


@app.route("/service5")
def service5():
