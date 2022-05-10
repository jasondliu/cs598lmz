import socket
import time

from . import constants as c
from . import exceptions

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._socket = socket.socket()

    def connect(self):
        try:
            self._socket.connect((self.host, self.port))
        except socket.error as e:
            raise exceptions.ClientError(e)

    def close(self):
        try:
            self._socket.close()
        except socket.error as e:
            raise exceptions.ClientError(e)

    def _read(self):
        result = self._socket.recv(1024).decode()
        if result == '':
            raise exceptions.ClientError('Server connection closed')
        status, data = result.split('\n', 1)
        if status == c.STATUS_OK:
            return data
        elif status == c.STATUS_ERROR:
            raise exceptions.ClientError(data)
