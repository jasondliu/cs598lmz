import socket
# Test socket.if_indextoname()

import sys
import os
import unittest
from test import support
from test.support import import_module

try:
    import_module('idna')
except ImportError:
    raise unittest.SkipTest("need idna module")

if sys.platform == "darwin":
    raise unittest.SkipTest("if_indextoname not supported on OSX")

class TestInterfaces(unittest.TestCase):

    def test_if_indextoname(self):

        # Some platforms (e.g. Linux) have a "dummy" interface with
        # index 1.  OSX does not, so we can't test that.
        if_indextoname = socket.if_indextoname
        try:
            name = if_indextoname(1)
        except OSError as e:
            if e.errno == errno.EINVAL:
                raise unittest.SkipTest("no dummy interface")
            raise
