import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOBaseTest(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        class MyIO(io.RawIOBase):
            def __init__(self):
                self.readinto_calls = 0
            def readinto(self, b):
                self.readinto_calls += 1
                return 0
        io_obj = MyIO()
        b = bytearray(5)
        self.assertEqual(io_obj.readinto(b), 0)
        self.assertEqual(io_obj.readinto_calls, 1)
        self.assertEqual(io_obj.readinto(memoryview(b)), 0)
        self.assertEqual(io_obj.readinto_calls, 2)
        self.assertRaises(TypeError, io_obj.readinto, b"")
        self.assertRaises(TypeError, io_obj.readinto, "")
        self.assertRaises(TypeError, io_
