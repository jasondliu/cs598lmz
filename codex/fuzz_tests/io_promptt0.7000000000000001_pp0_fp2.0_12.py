import io
# Test io.RawIOBase

class TestRawIOBase(unittest.TestCase):
    def test_constructor(self):
        # By default, a RawIOBase instance is not open for reading or writing
        b = io.RawIOBase()
        self.assertFalse(b.readable())
        self.assertFalse(b.writable())
        self.assertFalse(b.seekable())
        # But it can be changed by passing in the right arguments
        b = io.RawIOBase(readable=True)
        self.assertTrue(b.readable())
        self.assertFalse(b.writable())
        self.assertFalse(b.seekable())
        b = io.RawIOBase(writable=True)
        self.assertFalse(b.readable())
        self.assertTrue(b.writable())
        self.assertFalse(b.seekable())
        b = io.RawIOBase(readable=True, writable=True)
        self.assertTrue(b.readable())
        self.assertTrue(b.writable())
        self.assertFalse(b.seekable())
