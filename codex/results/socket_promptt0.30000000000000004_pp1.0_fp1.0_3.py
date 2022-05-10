import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket

from test import support
from test.support import import_module

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'test needs socket.if_indextoname()')
class IfIndextoNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        if_indextoname = socket.if_indextoname
        if_nametoindex = socket.if_nametoindex

        # Get the list of all available interfaces.
        try:
            import fcntl
        except ImportError:
            try:
                import ctypes
            except ImportError:
                self.skipTest('need fcntl or ctypes')
            else:
                SIOCGIFCONF = 0x8912
                MAXBYTES = 8096
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                names = array.array('B', b'\0
