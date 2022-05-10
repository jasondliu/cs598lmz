import socket
# Test socket.if_indextoname()
# (Linux only)

import os, sys
import unittest
import test.test_support

interface_name = test.test_support.import_module('socket').interface_name

class TestLinuxSpecific(unittest.TestCase):

    def testIfIndextoname(self):
        # This test requires Linux.
        if os.name != 'posix' or sys.platform != 'linux2':
            self.skipTest("Linux specific test")
        # get the loopback interface index
        loindex = socket.if_nametoindex("lo")
        # get the loopback interface name
        name = socket.if_indextoname(loindex)
        # make sure they are the same
        self.assertEqual(name, "lo")

    def testInterfaceName(self):
        # This test requires Linux.
        if os.name != 'posix' or sys.platform != 'linux2':
            self.skipTest("Linux specific test")
        # get the loopback interface index
        loindex = socket.if_nametoindex("lo")

