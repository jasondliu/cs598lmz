import io
# Test io.RawIOBase.
import io
import unittest

class RawIOTest(unittest.TestCase):
    def test_write(self):
        self.assertEqual(io.RawIOBase.write(None, b""), None)

    def test_writelines(self):
        self.assertEqual(io.RawIOBase.writelines(None, []), None)

    def test_readall(self):
        self.assertEqual(io.RawIOBase.readall(None), b"")

    def test_readinto(self):
        # Test that readinto has the same args as readinto().
        self.assertEqual(io.RawIOBase.readinto(None, None), 0)

    def test_read(self):
        self.assertEqual(io.RawIOBase.read(None, 0), b"")

    def test_readall(self):
        self.assertEqual(io.RawIOBase.readall(None), b"")

    def test_readline(self):
        self.assertEqual(io.RawIO
