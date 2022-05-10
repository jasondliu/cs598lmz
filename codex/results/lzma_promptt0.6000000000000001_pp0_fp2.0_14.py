import lzma
# Test LZMADecompressor with various file types.

class TestLZMA(unittest.TestCase):

    def test_read_eof(self):
        # Read one byte at a time from an uncompressible file until EOF.
        with open(TESTFN, 'wb') as f:
            f.write(b'\x00' * 10000)
        with open(TESTFN, 'rb') as f:
            d = lzma.LZMADecompressor()
            for i in range(10000):
                self.assertEqual(d.decompress(b'\x00'), b'\x00')
            self.assertEqual(d.decompress(b'\x00', 1), b'')
            self.assertEqual(d.unused_data, b'\x00')
            self.assertEqual(d.decompress(b'\x00'), b'')
            self.assertEqual(d.unused_data, b'\x00\x00')
        os.remove(TESTFN)

    def test_read
