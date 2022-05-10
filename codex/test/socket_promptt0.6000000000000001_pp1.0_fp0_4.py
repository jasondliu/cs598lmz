import socket
# Test socket.if_indextoname() and socket.if_nametoindex()

import os
import unittest
import sys
import socket
import subprocess

from test import test_support

IFNAMSIZ = 16

# This test checks that the socket.if_indextoname() and
# socket.if_nametoindex() functions work properly.
#
# This test is Linux-specific, and relies on the existence of the
# 'ip' command.

class IfconfigTests(unittest.TestCase):
    def setUp(self):
        # Run ifconfig -a and save the output.
        p = subprocess.Popen(["ifconfig", "-a"],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        self.names = []
        self.indices = []
        for line in p.stdout.readlines():
            if sys.version_info[0] < 3:
                line = line.decode("utf-8")
            words = line.split()
