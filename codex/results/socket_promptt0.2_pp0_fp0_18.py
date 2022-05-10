import socket
# Test socket.if_indextoname()

import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        #
        # This test will fail if the machine has no interfaces
        # (e.g. a router)
        try:
            socket.if_indextoname(1)
        except OSError as msg:
            if msg.errno == errno.EINVAL:
                self.skipTest('no interfaces on this machine')
            raise

    def test_if_indextoname_invalid_index(self):
        # Test if_indextoname() with invalid index
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 65536)

if __name__ == "__main__":
    un
