import io
# Test io.RawIOBase.
class RawIOBaseTest(unittest.TestCase):
    def test_rawiobase_attributes(self):
        # RawIOBase defines read, readinto, write and seek, which should be
        # attributes
        self.assertTrue(hasattr(io.RawIOBase, "read"))
        self.assertTrue(hasattr(io.RawIOBase, "readinto"))
        self.assertTrue(hasattr(io.RawIOBase, "write"))
        self.assertTrue(hasattr(io.RawIOBase, "seek"))

    def test_rawiobase_unseekable(self):
        # Issue #11459
        class Unseekable(io.RawIOBase):
            def read(self, n=-1):
                return b"0" * n
        self.assertRaises(io.UnsupportedOperation, Unseekable().seek, 0)
        self.assertRaises(io.UnsupportedOperation, Unseekable().seek, 0, 0)

    def test_newlines(self):
        for nl in (None, '', '\
