import io
# Test io.RawIOBase

import _io

class TestRawIOBase(unittest.TestCase):
    def test_read(self):
        # Test that read() returns an empty bytes object on EOF
        rawio = _io.RawIOBase()
        self.assertEqual(rawio.read(1), b'')
        self.assertEqual(rawio.read(0), b'')
        self.assertEqual(rawio.read(-1), b'')

    def test_readinto(self):
        # Test that readinto() returns 0 on EOF
        rawio = _io.RawIOBase()
        b = bytearray(1)
        self.assertEqual(rawio.readinto(b), 0)
        self.assertEqual(rawio.readinto(b), 0)
        self.assertEqual(rawio.readinto(b), 0)

    def test_readinto_resize(self):
        # Test that readinto() resizes the buffer
        rawio = _io.RawIOBase()
        b = bytearray
