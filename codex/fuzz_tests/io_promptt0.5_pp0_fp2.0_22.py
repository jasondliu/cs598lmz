import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):

    def test_args(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_unsupported_operations(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.read)
        self.assertRaises(io.UnsupportedOperation, raw.readinto, b"")
        self.assertRaises(io.UnsupportedOperation, raw.readline)
        self.assertRaises(io.UnsupportedOperation, raw.write, b"")
        self.assertRaises(io.UnsupportedOperation, raw.seek, 0)
        self.assertRaises(io.UnsupportedOperation, raw.tell)
        self.assertRaises(io.UnsupportedOperation, raw.truncate)
        self.assertRaises(io.UnsupportedOperation, raw.fileno)
        self.assertRaises(io.UnsupportedOperation, raw.isatty)
        self.assertRaises(io.UnsupportedOperation,
