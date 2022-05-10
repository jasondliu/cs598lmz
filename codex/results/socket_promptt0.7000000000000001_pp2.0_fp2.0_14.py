import socket
# Test socket.if_indextoname()

from test_support import verbose, run_unittest
import unittest
import sys
from socket import AF_INET

class IfIndextoNameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        if verbose:
            print '\nTesting socket.if_indextoname()'
        try:
            socket.if_indextoname(1)
        except socket.error:
            pass
        else:
            self.fail('Exception expected')

    def test_if_indextoname_invalid_args(self):
        self.assertRaises(TypeError, socket.if_indextoname)
        self.assertRaises(socket.error, socket.if_indextoname, 1, 2)


def test_main():
    try:
        run_unittest(IfIndextoNameTestCase)
    finally:
        if verbose:
            print "test_if_indextoname is done
