import io
# Test io.RawIOBase

class TestRawIO(TestIOBase):

    def test_rawiobase(self):
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, buffer(b''))
        self.assertRaises(io.UnsupportedOperation, rawio.write, b'')
        self.assertEqual(rawio.seekable(), False)
        self.assertEqual(rawio.readable(), False)
        self.assertEqual(rawio.writable(), False)
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate)
        self.assertRaises(io.UnsupportedOperation, rawio.flush)

        buf = io.BytesIO()
        rawio = io.RawIOBase(buf)
        self.assertE
