import io
# Test io.RawIOBase

import _io

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test reading
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"A")
        self.assertEqual(b.read(2), b"BC")
        self.assertEqual(b.read(3), b"DE")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(1), b"")
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(-1), b"ABCDE")
        self.assertEqual(b.read(-1), b"")
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(None), b"ABCDE")
        self.assertEqual(b.read(None), b"")
       
