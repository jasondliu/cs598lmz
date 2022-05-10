import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import sys
import errno

from test import test_support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, socket.if_indextoname() is not supported.
        if sys.platform == 'win32':
            self.assertRaises(socket.error, socket.if_indextoname, 0)
            return

        # On Linux, socket.if_indextoname() is supported.
        # On Linux, socket.if_indextoname() returns the name of the
        # interface corresponding to the given index.
        # On Linux, socket.if_indextoname() raises OSError if the
        # given index is invalid.
        # On Linux, socket.if_indextoname() raises OSError if the
        # given index is valid but the interface is not up.
        # On Linux, socket.if_indextoname() raises OSError if the
        # given
