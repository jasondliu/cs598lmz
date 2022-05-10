import io
# Test io.RawIOBase-like class with readinto.

from test import support
import unittest

class ReadintoIO(io.RawIOBase):
    def __init__(self, value_to_return, target_buffer):
        self.value_to_return = value_to_return
        self.target_buffer = target_buffer
        self.closed = False

    def close(self):
        self.closed = True

    def readinto(self, byte_view):
        byte_view[:self.value_to_return] = self.target_buffer
        return self.value_to_return

class RawIOTest(unittest.TestCase):
    def test_simple(self):
        ri = ReadintoIO(3, b'foo')
        b = bytearray(5)
        self.assertEqual(ri.readinto(b), 3)
        self.assertEqual(b, bytearray(b'foof\x00'))
        ri.close()
        self.assertTrue(ri.closed)

    def test_ex
