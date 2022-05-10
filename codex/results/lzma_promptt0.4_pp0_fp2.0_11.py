import lzma
# Test LZMADecompressor.read() with a small amount of data.

class TestReadSmall(unittest.TestCase):
    def test_read(self):
        data = b"".join(
            [bytes([x]) * x for x in range(1, 256)]
            + [bytes([x]) * (255 - x) for x in range(1, 256)]
            )
        compressed = lzma.compress(data)
        for i in range(1, len(compressed)):
            d = lzma.LZMADecompressor()
            self.assertEqual(d.read(i), data[:i])
            self.assertEqual(d.unused_data, compressed[i:])
            self.assertEqual(d.read(), data[i:])
            self.assertEqual(d.unused_data, b"")
            self.assertEqual(d.read(), b"")
            self.assertEqual(d.unused_data, b"")

# Test LZMADecompressor.read() with a large amount of
