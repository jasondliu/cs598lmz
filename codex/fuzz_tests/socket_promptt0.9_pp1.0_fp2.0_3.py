import socket
# Test socket.if_indextoname function.
import unittest
# Import tests.support for generic testing support and check_syntax().
from test import support
from test.support import check_syntax
import warnings


class IfNameToIndexTestCase(unittest.TestCase):

    def test_integers(self):
        with self.assertRaises(TypeError):
            socket.if_indextoname(1)
        with self.assertRaises(TypeError):
            socket.if_indextoname(True)
        with self.assertRaises(TypeError):
            socket.if_indextoname(1L)
        with self.assertRaises(TypeError):
            socket.if_indextoname(1.0)

    def test_strings(self):
        with self.assertRaises(TypeError):
            socket.if_indextoname('\000')

    def test_errors(self):
        with self.assertRaises(OverflowError):
            socket.if_indextoname(-1)


class MiscModuleFunctionTestCase(unittest.Test
