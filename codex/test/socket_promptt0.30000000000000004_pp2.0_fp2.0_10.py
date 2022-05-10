import socket
# Test socket.if_indextoname()
#
# This test case is for the function socket.if_indextoname()
#
# Author: Qiaowei Ren <qiaowei@redhat.com>

import os
import sys
import unittest
import socket
from testlib import *
from network import *

class TestSocketIfIndextoname(unittest.TestCase):
    def setUp(self):
        self.ifname = get_unused_ifname()
        self.ifindex = get_unused_ifindex()
        self.ifindex2 = get_unused_ifindex()
        self.ifindex3 = get_unused_ifindex()

    def tearDown(self):
        del_ifname(self.ifname)
        del_ifindex(self.ifindex)
        del_ifindex(self.ifindex2)
        del_ifindex(self.ifindex3)

    def test_if_indextoname(self):
        """
        Test if_indextoname() function
        """
        # Create a new interface
       
