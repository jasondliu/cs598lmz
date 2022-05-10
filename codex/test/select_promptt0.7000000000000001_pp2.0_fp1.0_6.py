import select
# Test select.select
import socket
import sys
import threading
import time


class EchoServer(threading.Thread):

    def __init__(self, family, stype, proto=0):
        super().__init__()
        self.addr = ('', 0)
        self.family_name = {
            socket.AF_INET: 'AF_INET',
            socket.AF_INET6: 'AF_INET6',
            socket.AF_UNIX: 'AF_UNIX',
        }[family]
        self.type_name = {
            socket.SOCK_STREAM: 'SOCK_STREAM',
            socket.SOCK_DGRAM: 'SOCK_DGRAM',
            socket.SOCK_RAW: 'SOCK_RAW',
        }[stype]
        self.sock = socket.socket(family, stype, proto)
        self.sock.bind(self.addr)
        self.sock.listen(1)

    def fileno(self):
        return self.sock.fileno()

