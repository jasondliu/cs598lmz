import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
import test.support
import platform

if_indextoname = socket.if_indextoname

@unittest.skipUnless(hasattr(socket, 'if_indextoname'),
                     'test needs socket.if_indextoname()')
class IfIndextoNameTest(unittest.TestCase):

    def test_basic(self):
        # Issue #7998: Check that if_indextoname() works.
        #
        # The test is not reliable, as the network interfaces
        # may not be available.
        #
        # On Linux, the test will only work if the network
        # interfaces are configured.
        #
        # On Windows, the test will only work if the network
        # interfaces are configured.
        #
        # On OSX, the test will only work if the network
        # interfaces are configured.
        #
        # On FreeBSD, the test will only work if the network
        # interfaces are configured.
        #
        # On OpenBSD, the test will only
