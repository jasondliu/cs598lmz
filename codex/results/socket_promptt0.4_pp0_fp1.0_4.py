import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import test.support
from test.support import TESTFN, run_unittest

if_indextoname = socket.if_indextoname
if_nametoindex = socket.if_nametoindex

class IfnameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # On some systems, the first interface is called 'lo'.
        # On others, it's called 'lo0'.
        # Try to detect the difference.
        lo = if_indextoname(1)
        if lo == 'lo0':
            self.assertEqual(if_indextoname(1), 'lo0')
            self.assertEqual(if_nametoindex('lo0'), 1)
        else:
            self.assertEqual(lo, 'lo')
            self.assertEqual(if_indextoname(1), 'lo')
            self.assertEqual(if_nametoindex('lo'), 1)

    def test_invalid_if_
