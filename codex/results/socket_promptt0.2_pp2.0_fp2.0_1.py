import socket
# Test socket.if_indextoname()

import unittest
from test import support
from test.support import import_module

socket = import_module('socket')

class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname)
        self.assertTrue(isinstance(ifname, str))

def test_main():
    support.run_unittest(TestIfIndextoname)

if __name__ == "__main__":
    test_main()
