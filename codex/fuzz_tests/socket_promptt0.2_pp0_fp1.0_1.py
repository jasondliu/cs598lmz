import socket
# Test socket.if_indextoname()

import sys
import os
import unittest
import socket
import errno
import array
import struct
import subprocess

from test import test_support
from test.test_support import TESTFN, run_unittest, import_module

# Skip test if no if_indextoname()
if not hasattr(socket, 'if_indextoname'):
    raise test_support.TestSkipped("Platform has no socket.if_indextoname()")

# Skip test if no if_nametoindex()
if not hasattr(socket, 'if_nametoindex'):
    raise test_support.TestSkipped("Platform has no socket.if_nametoindex()")

class IfIndextonameTest(unittest.TestCase):
    def test_if_indextoname(self):
        # Test socket.if_indextoname()
        # Get all interface indices
        ifreqs = array.array('B', '\0' * 4096)
        try:
            f = open('/proc/net/dev', 'r')
