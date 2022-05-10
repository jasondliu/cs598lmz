import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import import_module

try:
    import threading
except ImportError:
    threading = None

class RawIOTest(unittest.TestCase):
    # File-like objects that support seek() and tell()
    # are tested in test_io.py

    def test_read(self):
        # Test RawIOBase.read()
        class TestRawIO(io.RawIOBase):
            def __init__(self):
                self.read_stack = []
            def readinto(self, buf):
                try:
                    data = self.read_stack.pop(0)
                except IndexError:
                    return 0
                n = len(data)
                buf[:n] = data
                return n
        rawio = TestRawIO()
        rawio.read_stack.append(b"abcde")
        rawio.read_stack.append(b"fghij")
        rawio.read_stack.append(b"klmno")
        self.assertEqual
