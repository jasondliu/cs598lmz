import socket
# Test socket.if_indextoname()
# Bug #2979: segfault in socket.if_indextoname on python 2.6.1 (OSX 10.6.2)

# This bug is fixed in Python 2.6.6.
import sys
if sys.version_info < (2, 6, 6):
    print("skipped for Python < 2.6.6")
    sys.exit(0)

import os
import unittest

from test.support import TESTFN, run_unittest, import_module

@unittest.skipIf(import_module('ctypes') is None, 'requires ctypes')
class IfIndextoNameTestCase(unittest.TestCase):
    def test_if_indextoname(self):
        err = None
        try:
            socket.if_indextoname(0)
        except OSError as e:
            err = e

        # If err is an OSError, it should be EINVAL.
        if err is not None:
            self.assertEqual(err.errno, err
