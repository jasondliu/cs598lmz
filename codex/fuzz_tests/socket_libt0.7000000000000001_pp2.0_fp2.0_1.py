import socket

from . import api


class BaseServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._sock = None

    def start(self, on_listen):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((self.host, self.port))
        self._sock.listen(10)

        self.on_listen = on_listen

        return self

    def serve_forever(self):
        while True:
            try:
                conn, addr = self._sock.accept()
                self.on_listen(conn, addr)
            except Exception as e:
                print(e)

    def close(self):
        if self._sock:
            self._sock.close()


class ProxyServer(BaseServer):
