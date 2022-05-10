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
