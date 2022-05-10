import select
# Test select.select, poll and epoll
import socket
import sys
import threading
import time
import unittest

from test import support
from test.support import find_unused_port

HOST = support.HOST
MSG = b"foo\n"
MSG_LEN = len(MSG)


class ThreadedTCPServer(socketserver.ThreadingMixIn,
                        socketserver.TCPServer):
    pass


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        cur_thread = threading.current_thread()
        data = self.request.recv(1024)
        self.server.data[cur_thread] = data


class MyTCPServer(socketserver.TCPServer):
    def server_activate(self):
        self.server_address = (self.server_address[0],
                               self.request_queue_size)
        socketserver.TCPServer.server_activate(self)

    def handle_error(self, request, client_address):
        self.close_
