import socket
# Test socket.if_indextoname()

import sys, os
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # On Windows, the loopback interface has index 1.
        # On other systems, it has index 2.
        # See issue #7995.
        if os.name == 'nt':
            self.assertEqual(socket.if_indextoname(1), 'lo')
        else:
            self.assertEqual(socket.if_indextoname(2), 'lo')

def test_main():
    support.run_unittest(IfIndextonameTest)

if __name__ == '__main__':
    test_main()
