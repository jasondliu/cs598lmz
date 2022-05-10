import socket
# Test socket.if_indextoname()
#
# This test case is supposed to be run on a Linux system.

try:
    socket.if_indextoname(0)
except socket.error:
    # Python socket module was compiled without HAVE_IF_INDEXTONAME
    raise unittest.SkipTest("Python socket module was compiled without HAVE_IF_INDEXTONAME")

import os, sys
if sys.platform == 'linux':
    import fcntl

@unittest.skipUnless(sys.platform == 'linux',
                     'Linux specific test')
class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Basic test
        self.assertEqual(socket.if_indextoname(1), b'lo')
        self.assertEqual(socket.if_indextoname(1), 'lo')

        # Test for invalid index
        with self.assertRaises(socket.error) as cm:
            socket.if_indextoname(0)
        self.assertEqual(cm.
