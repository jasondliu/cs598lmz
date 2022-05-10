import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Issue #7995: if_indextoname() should return None if the index is not
        # found.
        self.assertIsNone(socket.if_indextoname(0))
        self.assertIsNone(socket.if_indextoname(1))
        self.assertIsNone(socket.if_indextoname(-1))
        self.assertIsNone(socket.if_indextoname(2**32))
        self.assertIsNone(socket.if_indextoname(2**64))

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
