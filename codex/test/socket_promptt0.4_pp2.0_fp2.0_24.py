import socket
# Test socket.if_indextoname()
import sys
import test_support
import unittest

class IfIndextonameTestCase(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, if_indextoname() returns the network interface's
        # friendly name.
        if sys.platform == 'win32':
            self.assertTrue(socket.if_indextoname(1))
        # On other platforms, if_indextoname() returns the network
        # interface's name.
        else:
            self.assertTrue(socket.if_indextoname(1))

    def test_if_indextoname_invalid_index(self):
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)

def test_main():
    test_support.run_unittest(IfIndextonameTestCase)

if __name__ == '__main__':
    test_main()
