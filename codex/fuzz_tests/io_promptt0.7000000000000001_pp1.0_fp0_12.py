import io
# Test io.RawIOBase subclass

class TestRawIOBase(BaseTestIOBase):

    def test_rawiobase(self):
        # Test RawIOBase, the abstract base class for raw binary I/O.
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase)

    def test_attributes(self):
        # All RawIOBase derived classes must have these attrs
        RawIOBase = io.RawIOBase
        f = RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.fileno)
        self.assertRaises(io.UnsupportedOperation, f.isatty)
        self.assertRaises(io.UnsupportedOperation, f.read, 0)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, f.readline)
        self.assertRaises(io.UnsupportedOperation, f.seek, 0)
        self.assertRaises(io.UnsupportedOperation, f.tell)
        self.assertRaises
