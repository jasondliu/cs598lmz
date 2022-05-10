import socket
# Test socket.if_indextoname()

import socket
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Skip test if no interface name can be found.
try:
    socket.if_indextoname(1)
except OSError:
    raise unittest.SkipTest("requires an interface with index 1")

class InterfaceTest(unittest.TestCase):

    def testIfName(self):
        with support.captured_output("stderr") as s:
            self.assertIsNone(socket.if_nameindex())
        self.assertIn("if_nameindex", s.getvalue())

        with support.captured_output("stderr") as s:
            self.assertIsNone(socket.if_nametoindex("lo"))
        self.assertIn("if_nametoindex", s.getvalue())

        with support.captured_output("stderr") as s:
            self.assertEqual(socket.if_indextoname(1), "lo")
