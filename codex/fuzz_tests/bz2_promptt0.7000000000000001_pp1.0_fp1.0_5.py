import bz2
# Test BZ2Decompressor with multiple members

class TestBZ2Decompressor(unittest.TestCase):

    def test_decompress_multiple(self):
        d = bz2.BZ2Decompressor()
        data = d.decompress(bz2.compress(b"foo") + bz2.compress(b"bar"))
        self.assertEqual(data, b"foobar")

    def test_decompress_multiple_with_unused_data(self):
        d = bz2.BZ2Decompressor()
        data = d.decompress(bz2.compress(b"foo")[:3] + bz2.compress(b"bar"))
        self.assertEqual(data, b"foobar")

    def test_decompress_multiple_with_unused_data2(self):
        d = bz2.BZ2Decompressor()
        data = d.decompress(bz2.compress(b"foo") + bz2.compress(b"bar")[:3
