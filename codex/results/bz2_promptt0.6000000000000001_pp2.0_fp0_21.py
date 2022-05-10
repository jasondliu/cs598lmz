import bz2
# Test BZ2Decompressor.decompress()

class TestDecompressor:
    def test_decompress_with_no_data(self):
        d = bz2.BZ2Decompressor()
        self.assertEqual(d.decompress(b''), b'')
        self.assertEqual(d.decompress(b'\x42\x5a\x68'), b'')
        self.assertEqual(d.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'), b'')
        self.assertEqual(d.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59\x26\x53\x59'), b'')
        self.assertEqual(d.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59\x26
