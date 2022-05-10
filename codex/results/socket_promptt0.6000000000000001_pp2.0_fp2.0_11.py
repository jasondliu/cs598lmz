import socket
# Test socket.if_indextoname()
# This test is only valid if the system has at least one network interface.

import sys
import unittest
from test import support
from test.support import verbose

skip_expected = False
try:
    socket.if_indextoname(1)
except (ValueError, OSError):
    skip_expected = True

class If_indextonameTest(unittest.TestCase):

    @unittest.skipIf(skip_expected,
                     'This system does not have at least one network interface.')
    def test_if_indextoname(self):
        try:
            name = socket.if_indextoname(1)
        except Exception:
            self.fail("if_indextoname() failed")
        if verbose:
            print("name:", name)
        self.assertTrue(isinstance(name, str))

    @unittest.skipIf(skip_expected,
                     'This system does not have at least one network interface.')
    def test_if_indextoname_invalid(self
