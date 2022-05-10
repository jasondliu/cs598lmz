import select
# Test select.select() on a socket that is closed by the server.
import unittest
from test import test_support
import socket
import time

HOST = test_support.HOST

def server(evt, serv):
    conn, addr = serv.accept()
    print "Connection from", addr
    evt.wait()
    conn.close()
    serv.close()
    print "Server done"

class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv.setblocking(0)
        self.port = test_support.bind_port(self.serv)
        self.evt = threading.Event()
        threading.Thread(target=server, args=(self.evt, self.serv)).start()

    def tearDown(self):
        self.evt.set()
        self.serv.close()

    def test_interrupt(self):
        # XXX This test is non-deterministic: it
