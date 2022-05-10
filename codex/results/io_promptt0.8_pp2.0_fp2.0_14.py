import io
# Test io.RawIOBase.readall()
import random
import sys
import unittest

import test.support

class RawIOTestCase(unittest.TestCase):
    def setUp(self):
        self.data = b'\x00\x01\x02'
        self.obj = io.BytesIO()
        self.obj.write(self.data)
        self.obj.seek(0)

    def readall_test(self, func):
        self.assertEqual(b'', func(-1))
        self.assertEqual(b'', func(0))
        self.assertEqual(b'\x00', func(1))
        self.assertEqual(b'\x00\x01', func(2))
        self.assertEqual(b'\x00\x01\x02', func(3))
        self.assertEqual(b'\x00\x01\x02', func(4))
        self.assertEqual(b'\x00\x01\x02', func(sys.maxsize))

    def
