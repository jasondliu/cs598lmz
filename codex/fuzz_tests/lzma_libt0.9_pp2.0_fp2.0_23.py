import lzma
lzma.LZMA_AVAILABLE=True

uncompressed_size = 10000000
compressed_size = 1713420

@need_lzma
class LzmaTestcase(unittest.TestCase):
    def test_compress(self):
        with tempfile.TemporaryFile() as uncompressedFile:
            with tempfile.TemporaryFile() as compressedFile:
                uncompressedFile.write(bytes.fromhex('0001f3ff' * 50000))
                uncompressedFile.seek(0)
                with lzma.open(compressedFile, 'w', check=lzma.CHECK_NONE, preset=0) as lz:
                    shutil.copyfileobj(uncompressedFile, lz)
                    uncompressedFile.seek(0)
                compressedFile.seek(0)
                with lzma.open(compressedFile, 'r') as lz:
                    uncompressed = lz.read()
                    self.assertEqual(uncompressedFile.read(), uncompressed)

    def test_unsupoorted_check
