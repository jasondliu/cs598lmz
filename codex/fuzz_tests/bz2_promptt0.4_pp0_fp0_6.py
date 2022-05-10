import bz2
# Test BZ2Decompressor.__init__()

class TestBZ2DecompressorInit(unittest.TestCase):

    def test_init(self):
        bz2.BZ2Decompressor()


# Test BZ2Decompressor.decompress()

class TestBZ2DecompressorDecompress(unittest.TestCase):

    def test_decompress(self):
        d = bz2.BZ2Decompressor()
        self.assertRaises(IOError, d.decompress, b"garbage")
        self.assertEqual(d.decompress(bz2.compress(b"foo")), b"foo")
        self.assertEqual(d.decompress(b""), b"")
        self.assertEqual(d.decompress(b"\x00\x00\x00\x01\x00\x00\x00\x00"), b"")
        self.assertRaises(ValueError, d.decompress, b"\x00\x00\x00\x01\
