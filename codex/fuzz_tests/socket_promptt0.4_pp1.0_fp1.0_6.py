import socket
# Test socket.if_indextoname()
#
# This test checks that socket.if_indextoname() returns the correct
# interface name for a given index.
#
# The test is run in two parts. The first part checks that the function
# works for the loopback interface. The second part checks that the
# function works for the first non-loopback interface.
#
# This test is only run if socket.if_indextoname() is available.
#
# The test is currently only supported on Linux.

import unittest
import errno
import platform
import os
import sys
import subprocess
import socket
import time

from test.support import requires, run_unittest, find_unused_port, \
    get_attribute

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'socket.if_indextoname() required')
@unittest.skipUnless(sys.platform.startswith('linux'),
                     'Linux specific test')
class IfIndextonameTest(unittest.TestCase):

    def test_if_
