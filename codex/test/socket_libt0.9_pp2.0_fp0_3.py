import socket
from flask import Flask, request
import sys

app = Flask(__name__)

class DataSubscriber:
    def __init__(self, port, host='localhost', periodic_callback=None):
        self.port = port
        self.host = host
        self.periodic_callback = periodic_callback
        self.data_count = 0
        self.periodic_count = 0
        self.period_length = 0
        self.time_stamp = 0
        self.first_data_time=0;
        self.ready = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(1)

    def accept_new_connection(self):
        print("Listening for incoming connection on port {}".format(self.port))
        self.conn, self.address = self.s.accept()
        print("Got connection from {}".format(self.address))


