import selectors
import socket
import types

from . import utils


class Client:
    def __init__(self, address: str, port: int, nickname: str) -> None:
        self.address = address
        self.port = port
        self.nickname = nickname

    def run(self) -> None:
        self.sel = selectors.DefaultSelector()
        self.add_socket(self.nickname)

        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)

    def add_socket(self, nickname: str) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex((self.address, self.port))
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(
            connid=nickname,
            msg_total=
