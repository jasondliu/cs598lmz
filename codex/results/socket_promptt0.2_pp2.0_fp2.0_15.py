import socket
# Test socket.if_indextoname()

import os, sys
import unittest
import errno
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, if_indextoname() is only supported on Vista and later.
        if sys.platform == 'win32':
            if sys.getwindowsversion()[:2] < (6, 0):
                self.assertRaises(OSError, socket.if_indextoname, 0)
                return

        # On Linux, if_indextoname() is only supported on 2.6.18 and later.
        if sys.platform.startswith('linux'):
            if os.uname()[2] < '2.6.18':
                self.assertRaises(OSError, socket.if_indextoname, 0)
                return

        # On Solaris, if_indextoname() is only supported on 11 and later.
        if sys.platform == 'sunos5':
            if os.uname()[2
