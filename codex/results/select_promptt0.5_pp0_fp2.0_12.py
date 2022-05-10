import select
# Test select.select with a timeout.
import socket
import time
import unittest
from test import support

try:
    select.select
except AttributeError:
    raise unittest.SkipTest("test works only on systems with select()")

HOST = support.HOST
MSG = b"xxx"
BUFSIZE = 1024

class TestSelect(unittest.TestCase):
    def test_timeout(self):
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setblocking(False)
        serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serv.bind((HOST, 0))
        serv.listen(1)
        port = serv.getsockname()[1]
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.setblocking(False)
        conn.connect_ex((HOST, port))
        conn.send(MSG)
        #
        # With no timeout
