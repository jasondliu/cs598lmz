import select
# Test select.select on a socket with a timeout.
import socket
import sys
import time
import unittest
try:
    import threading
except ImportError:
    threading = None

from test import support

HOST = support.HOST

class SelectTestCase(unittest.TestCase):

    def test_error_conditions(self):
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [1], 2, 3)
        self.assertRaises(TypeError, select.select, [1], [2], 3)
        self.assertRaises(TypeError, select.select, [1], [2], [3])
        self.assertRaises(TypeError, select.select, [1, 2], [2], [3])
        self.assertRaises(TypeError, select.select, [1, 2], [2, 3], [3])
