import socket
# Test socket.if_indextoname()
#
# This test was initially added for issue #18962, but it was
# later fixed.  According to the issue, this test should
# raise a ValueError when the interface is not found, but
# it actually raises a SystemError.  The test is left here
# to make sure the bug is not reintroduced.

import socket
import unittest
from test import support


class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        self.assertRaises(SystemError, socket.if_indextoname, 1)


if __name__ == '__main__':
    unittest.main()
