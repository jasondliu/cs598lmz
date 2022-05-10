import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from test.support import os_helper

if_indextoname = support.import_module('socket').if_indextoname

class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('if_indextoname() not available')
        if not hasattr(socket, 'if_nameindex'):
            self.skipTest('if_nameindex() not available')
        if not hasattr(socket, 'if_nametoindex'):
            self.skipTest('if_nametoindex() not available')
        if not hasattr(socket, 'if_indextoname'):
            self.skipTest('if_indextoname() not available')
        if not hasattr(socket, 'if_nameindex'):
            self.skipTest('if_nameindex() not available')
        if not hasattr(socket
