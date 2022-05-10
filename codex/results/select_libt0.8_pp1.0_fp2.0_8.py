import selectors
import socket
import threading

from . import html
from . import http
from . import ws


class Server:
    def __init__(self, ipv4, port, host, root):
        self._ipv4 = ipv4
        self._port = port
        self._host = host
        self._root = root
        self._sel = selectors.DefaultSelector()
        self._clients = []

        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setblocking(False)
        self._server_socket.bind((ipv4, port))
        self._server_socket.listen(16)
        self._sel.register(self._server_socket, selectors.EVENT_READ, self._accept)

    def _accept(self, key, mask):
        conn, addr = key.fileobj.accept()
        conn.setblocking(False)
        key_conn = self._sel.selector.register(conn, selectors.EVENT_READ
