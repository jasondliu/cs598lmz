import select
from threading import Thread
import socket
import sys

from connectfour.common.protocol import ConnectFourClientProtocol, ConnectFourServerProtocol


def create_connection(host: str, port: int) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.connect((host, port))
    return sock


class ConnectFourClient(Thread):
    def __init__(self, host: str, port: int):
        super(ConnectFourClient, self).__init__()
        self._running = False
        self._protocol = ConnectFourClientProtocol()
        self._sock = create_connection(host, port)

    def run(self) -> None:
        self._running = True

        self._protocol.send_board(self._sock)
        while self._running:
            response = self._protocol.receive(self._sock)
            if not response:
                break
            print(response, end='')

        self._sock.close()

   
