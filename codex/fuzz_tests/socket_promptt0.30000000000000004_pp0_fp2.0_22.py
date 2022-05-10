import socket
# Test socket.if_indextoname()

import os, sys
import unittest
from test import support

class IfIndextonameTest(unittest.TestCase):

    def test_if_indextoname(self):
        ifname = socket.if_indextoname(1)
        self.assertIsInstance(ifname, str)
        self.assertTrue(len(ifname) > 0)

    def test_if_indextoname_invalid_index(self):
        with self.assertRaises(OSError) as cm:
            socket.if_indextoname(-1)
        self.assertEqual(cm.exception.errno, errno.EINVAL)

    def test_if_indextoname_invalid_type(self):
        with self.assertRaises(TypeError):
            socket.if_indextoname(None)

    def test_if_indextoname_invalid_type_2(self):
        with self.assertRaises(TypeError):
            socket.if_indextoname(1.0)

