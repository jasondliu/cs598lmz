import lzma
# Test LZMADecompressor.__init__()
# TODO: Make this test actually test something ...
# Currently, it just makes sure we don't crash on input we know
# decompresses fine.

class TestInit(unittest.TestCase):
    def test_has_check_passed(self):
        data = lzma.compress(b'foo')
        lzc = lzma.LZMADecompressor()
        output = lzc.decompress(data)
        self.assertEqual(output, b'foo')

    def test_incomplete_stream(self):
        data = lzma.compress(b'foo')
        lzc = lzma.LZMADecompressor()
        with self.assertRaises(EOFError):
            lzc.decompress(data[:-5])

    def test_stream_with_header(self):
        # cf. bug #14836
        data = lzma.compress(b'foo')
        data = b'\x00\r\r\r\r' +
