import select
# Test select.select() on a non-blocking socket.
import socket
import threading
import unittest
import time

from test.support import run_unittest, TESTFN, unlink

HOST = '127.0.0.1'
PORT = 54321

class BaseEintr(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName=methodName)

    def setUp(self):
        self.evt = threading.Event()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(0)
        try:
            self.sock.bind((HOST, PORT))
        except socket.error as err:
            if err.args[0] != errno.EADDRINUSE:
                raise
            # Perhaps the socket is still in TIME_WAIT.
            time.sleep(1)
