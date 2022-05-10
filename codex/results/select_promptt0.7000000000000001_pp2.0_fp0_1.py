import select
# Test select.select function in Windows.
import unittest
from select import error as select_error
from test import support

# Windows doesn't support the "exceptional condition" feature of select.
# So the third set of descriptors is ignored entirely.
# However, this means that we can't really test to see if an error
# occurs in that set of descriptors; as long as the first two sets
# work, the call should return successfully.

class SelTestCase(unittest.TestCase):
    def setUp(self):
        self.read_fds = []
        self.write_fds = []
        self.error_fds = []
        for i in range(5):
            rs, ws = socket.socketpair()
            self.read_fds.append(rs)
            self.write_fds.append(ws)
            self.error_fds.append(ws)
        for fd in self.read_fds[:3]:
            fd.send(b'x')

    def tearDown(self):
        for fd in self.read_f
