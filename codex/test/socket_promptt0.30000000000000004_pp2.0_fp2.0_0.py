import socket
# Test socket.if_indextoname()

import os
import sys
import unittest
from test import support
from test.support import import_module

if_indextoname = support.import_module('socket').if_indextoname

class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        self.assertEqual(if_indextoname(1), 'lo')
        self.assertEqual(if_indextoname(2), 'eth0')
        self.assertEqual(if_indextoname(3), 'eth1')
        self.assertEqual(if_indextoname(4), 'sit0')
        self.assertEqual(if_indextoname(5), 'lo')
        self.assertEqual(if_indextoname(6), 'eth0')
