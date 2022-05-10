import select
# Test select.select
# no timeout, no data present, test readfd
import unittest
from test import support

class TestSelect(unittest.TestCase):

    def accept(self, serv):
        serv.listen(1)
        conn, addr = serv.accept()
        conn.send(b"1")
        conn.close()

    def connect(self, host="127.0.0.1", port=0):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(0)
        # let the platform pick a port
        sock.bind((host, port))
        return sock

    def failUnlessRaisesErrno(self, err, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except OSError as x:
            if x.errno != err:
                self.fail('got errno %d (%s), expected %d' %
                          (x.errno, x.strerror, err))
