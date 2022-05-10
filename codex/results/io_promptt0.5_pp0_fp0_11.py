import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):
    def test_read(self):
        # Test that reading 0 bytes returns an empty bytes object, not b''
        # See http://bugs.python.org/issue1202
        rawio = io.RawIOBase()
        self.assertEqual(rawio.read(0), b'')

    def test_readinto(self):
        # Test that readinto with a buffer argument does not clear the buffer
        # See http://bugs.python.org/issue1202
        rawio = io.RawIOBase()
        b = bytearray(b"abcdef")
        self.assertEqual(rawio.readinto(b), 0)
        self.assertEqual(b, b"abcdef")

    def test_readinto_resize(self):
        # Test that readinto with a buffer argument does not resize the buffer
        # See http://bugs.python.org/issue1202
        rawio = io.RawIOBase()
        b = bytearray(b"abcdef")
       
