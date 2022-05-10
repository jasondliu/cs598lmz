import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.read)
        self.assertRaises(io.UnsupportedOperation, raw.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, raw.write, b'')
        self.assertRaises(io.UnsupportedOperation, raw.fileno)
        self.assertRaises(io.UnsupportedOperation, raw.seek, 0)
        self.assertRaises(io.UnsupportedOperation, raw.tell)
        self.assertRaises(io.UnsupportedOperation, raw.truncate)
        self.assertRaises(io.UnsupportedOperation, raw.readline)
        self.assertRaises(io.UnsupportedOperation, raw.flush)
        self.assertRaises(io.UnsupportedOperation, raw.close)

        self.assertFalse(raw.readable())
        self.assertFalse(raw.writable())
        self
