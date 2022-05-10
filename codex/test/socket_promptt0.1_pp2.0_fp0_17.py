import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import sys
import errno
import platform

from test import support
from test.support import import_module

# Skip test if there is no interface on this machine
support.get_attribute(socket, 'if_indextoname')

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'test needs socket.if_indextoname()')
class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Issue #7995: if_indextoname() should raise OSError with
        # errno.EINVAL if the index is invalid.
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)
        self.assertRaises(OSError, socket.if_indextoname, 1<<32)

