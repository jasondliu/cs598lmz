import bz2
# Test BZ2Decompressor with multiple kinds of objects.


class TestBZ2Decompressor:
    def test_decompress(self):
        text = bz2.decompress(bz2.compress(b'spam'))
        self.assertEqual(text, b'spam')

    def test_decompressor(self):
        source = bz2.compress(b'spam')
        d = bz2.BZ2Decompressor()
        text = d.decompress(source)
        text += d.decompress(b'')
        text += d.flush()
        self.assertEqual(text, b'spam')

    def test_large_decompress(self):
        text = b'A' * 1024 * 1024 * 1024 * 10
        text = bz2.decompress(bz2.compress(text))
        self.assertEqual(len(text), 10*1024*1024*1024)
        self.assertEqual(hash(text), hash(b'A' * 10*1024*1024*1024))


