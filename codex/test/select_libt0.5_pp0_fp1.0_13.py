import select
import socket
from threading import Thread
from time import sleep


class Client(object):
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((host, port), timeout)

    def close(self):
        self.sock.close()

    def get(self, key):
        try:
            self.sock.sendall(f'get {key}\n'.encode('utf8'))
            data = self.sock.recv(1024).decode('utf8')
            if data == 'None\n':
                return None
            return json.loads(data)
        except socket.error as err:
            raise ClientError('error', err)

