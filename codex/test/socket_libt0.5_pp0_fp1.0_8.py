import socket
import threading
import time

from . import common
from .common import MessageType
from .common import mk_msg
from .common import msg_type


class UDPServer(object):
    def __init__(self, host, port, msg_handler=None):
        self.host = host
        self.port = port
        self.msg_handler = msg_handler
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, port))
        self.stopped = False

    def _start_receiver(self):
        while not self.stopped:
            try:
                data, addr = self.sock.recvfrom(1024)
            except socket.error:
                print('Error receiving data')
                continue

            if not data:
                break

            if self.msg_handler:
                self.msg_handler(data, addr)

    def start(self):
        t = threading.Thread(target=self._start_receiver)
