import socket
# Test socket.if_indextoname()
import test.support
import unittest
import weakref

try:
    import fcntl
except (ImportError, AttributeError):
    pass

HOST = test.support.HOST
MSG = b"spam"
MSG_LEN = len(MSG)

def _check_socket_method(methodname):
    # raises skip_unless if specified socket method is missing
    getattr(socket.socket, methodname)

def close_on_del(sock):
    sock.close()

class SocketTCPTest(unittest.TestCase):

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = test.support.bind_port(self.serv)
        self.serv.listen(1)

    def tearDown(self):
        self.serv.close()
        self.serv = None

