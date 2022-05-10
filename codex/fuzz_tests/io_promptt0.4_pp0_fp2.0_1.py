import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_read(self):
        # test read()
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.read)
        self.assertRaises(io.UnsupportedOperation, r.read, 10)
        # test readinto()
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.readinto)
        self.assertRaises(io.UnsupportedOperation, r.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, r.readinto, array.array('b'))
        self.assertRaises(io.UnsupportedOperation, r.readinto, array.array('b', b'x' * 10))
        # test readall()
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.readall)
        # test read1()
        r = io.RawIOBase()
        self.assertRaises
