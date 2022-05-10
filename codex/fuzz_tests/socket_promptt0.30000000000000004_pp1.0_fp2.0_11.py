import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import socket
import select
import time
import struct
import random
import subprocess

from test import test_support
from test.test_support import TESTFN, run_unittest, import_module

# Skip test if no if_indextoname()
if not hasattr(socket, 'if_indextoname'):
    raise test_support.TestSkipped("if_indextoname() not defined")

class InterfaceTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = socket.if_indextoname(1)
        self.assertTrue(ifname is not None,
                        "if_indextoname(1) should not be None")
        self.assertTrue(ifname != '',
                        "if_indextoname(1) should not be ''")

    def test_if_nameindex(self):
        # Test if_nameindex()
        ifnameindex
