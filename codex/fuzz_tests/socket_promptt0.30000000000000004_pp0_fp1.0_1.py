import socket
# Test socket.if_indextoname()
#
# This test is only valid on Linux
#
# The test is to check that the function returns a non-zero value for
# a valid interface index, and a zero value for an invalid one.

import unittest
import os
import sys
import platform
import subprocess
import ctypes

from test import support

if not hasattr(socket, 'if_indextoname'):
    raise unittest.SkipTest("if_indextoname() not available")

if platform.system() != 'Linux':
    raise unittest.SkipTest("if_indextoname() only valid on Linux")

class IfIndexToNameTest(unittest.TestCase):

    def test_if_indextoname(self):
        # Get the interface index of lo
        lo_index = socket.if_nametoindex('lo')
        self.assertGreater(lo_index, 0)

        # Check that if_indextoname() returns the correct name for lo
        self.assertEqual(socket.if_indextoname(lo_index),
