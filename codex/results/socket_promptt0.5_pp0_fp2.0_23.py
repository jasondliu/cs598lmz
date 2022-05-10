import socket
# Test socket.if_indextoname()

import unittest
from test.support import run_unittest, socket_helper

class IfIndextonameTest(socket_helper.SocketTCPTest):

    def testIfIndextoname(self):
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 65536)
        self.assertRaises(OSError, socket.if_indextoname, 0xFFFFFFFF)

def test_main():
    run_unittest(IfIndextonameTest)

if __name__ == "__main__":
    test_main()
