import io
# Test io.RawIOBase

class TestRawIO(unittest.TestCase):

    # NB: the non-ASCII characters in the following tests are not claimed
    # to have any particular meaning.
    def _test_rawio_write(self, rawio, write_method, bs):
        # check write() with regular operation, and check that the buffer
        # is not modified if there's an error
        self.assertEqual(rawio.write(bs(b'abc')), 3)
        self.assertEqual(rawio.write(bs(b'')), 0)
        self.assertEqual(rawio.write(bs(b'def')), 3)
        self.assertEqual(rawio.write(bs(b'jklm')), 4)
        self.assertEqual(rawio.write(bs(b'nopqrstuvwxyz')), 13)
        self.assertEqual(rawio.write(bs(b'1')), 1)
        self.assertEqual(rawio.write(bs(b'23456789abcdef')),
