import select
# Test select.select() on a socket.
import socket
import sys
import threading
import time
import unittest

from test import test_support

HOST = test_support.HOST

class ThreadedEchoServer(threading.Thread):

    def __init__(self, test_object, host, port):
        threading.Thread.__init__(self)
        self.test_object = test_object
        self.host = host
        self.port = port

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        conn, addr = s.accept()
        while 1:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data)
        conn.close()
        s.close()
        self.test_object.ServerReady = True


class TestSelect(unittest.TestCase):

    def setUp(self):
        self
