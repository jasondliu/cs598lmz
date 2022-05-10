import io
# Test io.RawIOBase
import unittest

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        class TestRawIO(io.RawIOBase):
            def __init__(self, empty=False):
                self._empty = empty
            def readable(self):
                return True
            def readall(self):
                return b"" if self._empty else b"foobarbaz"
            def readinto(self, buf):
                data = self.readall()
                n = len(data)
                buf[:n] = data
                return n

        # Test a non-empty RawIO
        rawio = TestRawIO(empty=False)

        # Test that read() with no arguments returns all readable data
        self.assertEqual(rawio.read(), b"foobarbaz")

        # Test that read() with a too-large argument returns all readable data
        self.assertEqual(rawio.read(100), b"foobarbaz")

        # Test that read() with a positive argument returns up to that much data
        self.
