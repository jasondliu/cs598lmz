import io
# Test io.RawIOBase

import unittest

class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        # Test readinto()
        class TestRawIO(io.RawIOBase):
            def __init__(self, initial_bytes):
                self._bytes = initial_bytes
                self._read_offset = 0
            def readinto(self, buf):
                if self._read_offset >= len(self._bytes):
                    return None
                n = min(len(buf), len(self._bytes) - self._read_offset)
                buf[:n] = self._bytes[self._read_offset:self._read_offset+n]
                self._read_offset += n
                return n
        #
        b = bytearray(b'abcdefgh')
        f = TestRawIO(b)
        buf = bytearray(3)
        self.assertEqual(f.readinto(buf), 3)
        self.assertEqual(buf, b'abc')
        self.assertEqual(f.readinto
