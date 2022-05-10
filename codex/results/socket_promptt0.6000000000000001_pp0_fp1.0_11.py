import socket
# Test socket.if_indextoname()

import sys
import unittest
from test import support
from test.support import import_module
from test.support.script_helper import assert_python_ok

# Skip test if there is no network.
support.requires('network')

# Skip test if there is no ipv6 support.
import_module('ipaddress')

# On AIX, if_nametoindex() is not available.
skip_message = (
    "test_socket skipped -- "
    "if_indextoname() not available on this platform")
try:
    socket.if_indextoname(1)
except AttributeError:
    raise unittest.SkipTest(skip_message)


class TestExceptions(unittest.TestCase):

    def testErrors(self):
        self.assertRaises(ValueError, socket.if_indextoname, -1)
        self.assertRaises(ValueError, socket.if_indextoname, 0)
        self.assertRaises(OverflowError, socket.if_indextoname, sys.
