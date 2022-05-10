import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):

    def test_rawiobase(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))
        self.assertTrue(io.RawIOBase(None))
        self.assertRaises(OSError, io.RawIOBase, 1)

    def test_io_methods(self):
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, rawio.readline)
        self.assertRaises(io.UnsupportedOperation, rawio.write, b'')
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate)
       
