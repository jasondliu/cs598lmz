import select
import sys
import time

from lib.logger import logger

class SerialPort:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

        self.fd = None

    def open(self):
        self.fd = serial.Serial(self.port, self.baudrate)
        self.fd.flush()

    def close(self):
        self.fd.close()

    def send(self, data):
        self.fd.write(data)

    def recv(self, length):
        return self.fd.read(length)

    def recv_all(self, length):
        result = b''
        while len(result) < length:
            result += self.recv(length - len(result))
        return result

    def recv_until(self, delimiter):
        result = b''
        while delimiter not in result:
            result += self.recv(1)
        return result

    def recv_until_timeout(self, delimiter
