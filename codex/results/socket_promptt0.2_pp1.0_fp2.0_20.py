import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import sys
import errno
import platform

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname not defined")

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, if_indextoname() is only supported on Vista and later.
        if sys.platform == 'win32' and sys.getwindowsversion()[:2] < (6, 0):
            self.assertRaises(OSError, socket.if_indextoname, 0)
            return

        # On Linux, if_indextoname() is only supported on 2.6.19 and later.
        if sys.platform.startswith('linux') and \
           sys.version_info < (2, 6, 19):
            self.assertRaises(OSError, socket.if_indextoname, 0)
            return

        # On
