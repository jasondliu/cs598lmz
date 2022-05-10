from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

self._test_decompressor(LZMADecompressor, data)


class TestCompress(unittest.TestCase):
    def test_compress(self):
        with open(self.filename, 'rb') as f:
            data = f.read()
        compress = self.compressor()
        chunks = []
        for chunk in split_every(1024, data):
            chunks.append(compress.compress(chunk))
        chunks.append(compress.flush())
        self.assertEqual(b''.join(chunks), self.compressed)


def test_main():
    support.run_unittest(
        TestDecompress,
        TestBadInput,
    )


if __name__ == '__main__':
    test_main()
