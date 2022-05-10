import io
# Test io.RawIOBase.readall()

import sys
import unittest

class TestRawIOBaseReadall(unittest.TestCase):

    def test_readall_0(self):
        # Check that readall() returns an empty bytes object when the stream
        # is at EOF.
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                return 0
        raw = MyRawIO()
        self.assertEqual(raw.readall(), b'')

    def test_readall_1(self):
        # Check that readall() returns the entire contents of the stream.
        class MyRawIO(io.RawIOBase):
            def __init__(self):
                self.read_stack = [b'abc', b'def', b'ghi']
            def readable(self):
                return True
            def readinto(self, b):
                data = self.read_stack.pop(0)
                n = len(data)
                b[:n] = data
                return
