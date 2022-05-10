import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import errno
import sys

from test import test_support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, socket.if_indextoname() is only available for
        # Python 3.4+ and Windows 8+
        if sys.platform == 'win32' and sys.version_info < (3, 4):
            self.skipTest('socket.if_indextoname() is only available for '
                          'Python 3.4+ and Windows 8+')
        # On Windows, socket.if_indextoname() is only available for
        # Python 3.4+ and Windows 8+
        if sys.platform == 'win32' and sys.version_info < (3, 4):
            self.skipTest('socket.if_indextoname() is only available for '
                          'Python 3.4+ and Windows 8+')
        # On Windows, socket.if_indextoname() is only available
