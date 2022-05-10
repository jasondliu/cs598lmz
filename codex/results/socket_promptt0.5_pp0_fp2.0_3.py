import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import array
import errno
import select
import time
import struct
import subprocess
from test import support
from test.support import import_module

HOST = support.HOST

if_indextoname = socket.if_indextoname
if_nametoindex = socket.if_nametoindex

class NetworkAPITest(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        unittest.TestCase.__init__(self, methodName=methodName)
        # On OpenBSD >= 5.3, the default route is not necessarily on the
        # first interface, so we need to find the right one.
        self.default_if = None
        self.default_ip = None

    def setUp(self):
        if os.name != "posix":
            self.skipTest("POSIX specific tests")

    def tearDown(self):
        pass

    def test_if_indextoname(self):
        # Make sure if_ind
