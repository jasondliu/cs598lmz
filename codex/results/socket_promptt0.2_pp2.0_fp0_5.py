import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest('if_indextoname() not available')

class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        #
        # This test is not very robust.  It assumes that the first
        # interface is lo and that the second interface is eth0.
        #
        # This test also assumes that the first interface has index 1
        # and the second interface has index 2.  This is not guaranteed
        # by the interface.  It is only true on Linux.
        #
        # This test also assumes that the first interface is up and the
        # second interface is down.  This is not guaranteed by the
        # interface.  It is only true on Linux.
        #
        # This test also assumes that the first interface has a MAC
        # address and the second interface does not. 
