import socket
# Test socket.if_indextoname() on a loopback interface.

import os, sys
import unittest
from test.support import run_unittest, get_attribute, is_jython
from test import string_tests

try:
    if_indextoname = socket.if_indextoname
except AttributeError:
    raise unittest.SkipTest('if_indextoname not available')

class IfIndexToNameTest(unittest.TestCase):

    def testIfIndexToName(self):
        try:
            import fcntl
        except ImportError:
            if sys.platform == "win32":
                self.skipTest("fcntl not available on Windows")
            else:
                raise

        try:
            f = os.popen("/sbin/ifconfig -a", "r")
        except (OSError, IOError):
            raise unittest.SkipTest("ifconfig not available")

        interfaces = []
        for line in f:
            if line.lstrip().startswith("lo"):
                interfaces.append("lo")
               
