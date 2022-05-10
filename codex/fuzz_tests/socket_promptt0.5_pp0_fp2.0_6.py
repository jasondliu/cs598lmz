import socket
# Test socket.if_indextoname()

import sys
import unittest
from test import support

class IfIndextonameTestCase(unittest.TestCase):
    def test_if_indextoname(self):
        # Issue #7995: IP_MULTICAST_IF accepts an interface index
        # instead of a network interface name.
        name = socket.if_indextoname(1)
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)

    def test_if_indextoname_error(self):
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, sys.maxsize)

def test_main():
    support.run_unittest(IfIndextonameTestCase)

if __name__ == "__main__":
    test_main()
