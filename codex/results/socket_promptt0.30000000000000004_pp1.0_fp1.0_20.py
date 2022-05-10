import socket
# Test socket.if_indextoname()

import unittest
import socket
import os
import sys
import errno
import platform
import subprocess
from test import test_support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Issue #14097: if_indextoname() should raise OSError with
        # errno.ENXIO when the interface index is not valid.
        self.assertRaises(OSError, socket.if_indextoname, -1)
        self.assertRaises(OSError, socket.if_indextoname, 0)

    @unittest.skipUnless(hasattr(socket, 'if_nameindex'),
                         'if_nameindex() required')
    def test_if_nameindex(self):
        # Issue #14097: if_nameindex() should return an empty list
        # when there are no network interfaces.
        self.assertEqual(socket.if_nameindex(), [])

    @unittest.skipUnless(hasattr(socket, '
