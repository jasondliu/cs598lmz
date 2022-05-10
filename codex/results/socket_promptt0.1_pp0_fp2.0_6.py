import socket
# Test socket.if_indextoname()

import unittest
import os
import sys
import errno
import socket
import array
import struct
import select
import time
import platform
import subprocess
import re

from test import test_support
from test.test_support import TESTFN, run_unittest, import_module

HOST = test_support.HOST

class NetworkConnectionNoServer(unittest.TestCase):
    """Check that we can connect to a server that is not listening."""

    def setUp(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self):
        self.serv.close()

    def testConnect(self):
        # Connecting to a socket which isn't listening should fail with
        # ECONNREFUSED.
        try:
            self.serv.connect((HOST, test_support.find_unused_port()))
        except socket.error, e:
            self.assertEqual(e.errno, errno.ECONNREFUSED)

