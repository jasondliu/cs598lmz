import socket
import datetime
import time
import re

__author__ = 'Adrian Agnic'

class Sensor:
    def __init__(self, config):
        self.config = config
        self.sensor_id = config['sensor_id']
        self.host = config['host']
        self.port = config['port']
        self.interval = config['interval']
        self.last_read = None
        self.last_value = None
        self.last_check = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(10)

    def read_sensor_value(self):
        try:
            self.sock.connect((self.host, self.port))
            self.sock.sendall(b'GET / HTTP/1.1\r\n\r\n')
            data = self.sock.recv(1024)
            self.sock.close()
        except socket.timeout:
            return None

       
