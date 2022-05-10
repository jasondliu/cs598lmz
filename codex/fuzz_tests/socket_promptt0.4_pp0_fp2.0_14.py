import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest('if_indextoname not available')

if not hasattr(socket, 'if_nametoindex'):
    raise unittest.SkipTest('if_nametoindex not available')

class TestIfIndextoName(unittest.TestCase):
    def test_basic(self):
        # Test if_indextoname()
        try:
            socket.if_indextoname(1)
        except OSError:
            # The interface index 1 is not available
            pass
        else:
            # The interface index 1 is available
            self.assertEqual(socket.if_indextoname(1),
                             socket.if_indextoname(socket.if_nametoindex('lo')))

    def test_invalid_index(self):
        # Test if_indextoname() with invalid index
        self.assertRaises(Overflow
