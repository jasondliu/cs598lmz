import socket
# Test socket.if_indextoname().

from test_support import run_unittest
import unittest
import socket

class IfIndextonameTestCase(unittest.TestCase):

    def testInvalidArgs(self):
        self.assertRaises(TypeError, socket.if_indextoname)
        self.assertRaises(OverflowError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 10**9)

def test_main():
    run_unittest(IfIndextonameTestCase)

if __name__ == "__main__":
    test_main()
