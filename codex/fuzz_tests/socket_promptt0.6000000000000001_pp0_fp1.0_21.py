import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import socket
from test import support

if_indextoname_available = socket.if_indextoname is not None

@unittest.skipUnless(if_indextoname_available,
                     'if_indextoname not available')
class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        try:
            name = socket.if_indextoname(1)
        except OSError:
            # This test requires root privileges.
            self.skipTest('if_indextoname requires root privileges')
        self.assertIsNotNone(name)

if __name__ == '__main__':
    unittest.main()
