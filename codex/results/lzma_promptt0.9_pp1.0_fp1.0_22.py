import lzma
# Test LZMADecompressor


class TestLZMADecompressor(TestCase):

    def test_badargs(self):
        self.assertRaises(TypeError, lzma.LZMADecompressor, 42)

    def test_lzma_bytes(self):
        with open(TESTFN, 'wb') as f:
            f.write(b'.' * 15 + b'X' + b'.' * 127 + b'Y' + b'.' * 1023 + b'Z')
        with open(TESTFN, mode='rb') as f:
            self.assertEqual(lzma.decompress(f.read()),
                b'.' * 15 + b'X' + b'.' * 127 + b'Y' + b'.' * 1023 + b'Z')

    def test_arrays(self):
        import array
        with open(TESTFN, 'wb') as f:
            f.write(b'.' * 15 + b'X' + b'.' * 127 + b'Y' + b'.' * 1023 + b'Z
