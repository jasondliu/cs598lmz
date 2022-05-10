import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        # Test that read() returns an empty bytes object at EOF
        rawio = io.RawIOBase()
        self.assertEqual(rawio.read(1), b'')
        self.assertEqual(rawio.read(0), b'')
        self.assertEqual(rawio.read(-1), b'')
        self.assertEqual(rawio.read(), b'')
        self.assertEqual(rawio.read(sys.maxsize), b'')
        self.assertEqual(rawio.read(sys.maxsize + 1), b'')
        self.assertEqual(rawio.read(sys.maxsize + 2), b'')
        self.assertEqual(rawio.read(sys.maxsize + 3), b'')
        self.assertEqual(rawio.read(sys.maxsize + 4), b'')
        self.assertEqual(rawio.read(sys.maxsize + 5), b'')
