import socket
# Test socket.if_indextoname()
#
# This test is for Linux only.  It could be made to work on other
# platforms by adding a special case for them in the if_indextoname()
# function.

import unittest
import os
import sys
import socket
import subprocess
import errno
import time
import select
import signal
import gc
import traceback

from test import support
from test.support import import_module

if not hasattr(socket, "if_indextoname"):
    raise unittest.SkipTest("if_indextoname not available")

class BasicTests(unittest.TestCase):
    def test_name(self):
        # Test if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname is not None,
                        "if_indextoname() returned None")
        self.assertTrue(ifname.startswith(b"lo"),
                        "if_indextoname() returned %r" % ifname)
