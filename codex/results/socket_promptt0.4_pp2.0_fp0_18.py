import socket
# Test socket.if_indextoname()

from test_support import verbose
import unittest
import socket

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if not hasattr(socket, 'if_indextoname'):
            return

        # XXX(nnorwitz): I don't know how to test this without
        # hardcoding the interface name.  Perhaps we can get the
        # interface name from another function.
        if verbose:
            print 'if_indextoname(1) =', socket.if_indextoname(1)

        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(OverflowError, socket.if_indextoname, 2**32)

def test_main():
    test_support.run_unittest(IfIndextoNameTest)

if __name__ == "__main__":
    test_main()
