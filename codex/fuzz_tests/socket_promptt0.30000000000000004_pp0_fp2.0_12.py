import socket
# Test socket.if_indextoname
#
# $Id: if_indextoname.py,v 1.1 2004/07/19 08:46:58 aclement Exp $

import unittest
from test import test_support

class IfIndextonameTestCase(unittest.TestCase):

    def testIndextoname(self):
        # Issue #7995: if_indextoname should return None if the index is not
        # valid.
        self.assertEqual(socket.if_indextoname(-1), None)
        self.assertEqual(socket.if_indextoname(0), None)
        self.assertEqual(socket.if_indextoname(1), None)


def test_main():
    test_support.run_unittest(IfIndextonameTestCase)

if __name__ == "__main__":
    test_main()
