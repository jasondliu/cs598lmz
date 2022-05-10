import socket
# Test socket.if_indextoname()

import sys
import unittest
from test import support
from test.support import os_helper

if_indextoname = socket.if_indextoname

class TestIfIndextoname(unittest.TestCase):

    def test_if_indextoname(self):
        # Test if_indextoname()
        ifname = if_indextoname(1)
        self.assertTrue(isinstance(ifname, str),
                        'if_indextoname() returned invalid result')

    def test_if_indextoname_invalid_index(self):
        # Test if_indextoname() with invalid index
        with self.assertRaises(OSError) as cm:
            if_indextoname(999999)
        self.assertEqual(cm.exception.errno, os_helper.ENXIO)

