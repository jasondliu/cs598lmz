import lzma
lzma.LZMAError

import unittest

class TestCompression(unittest.TestCase):

    def test_uncompress_bytes(self):
        # this was the original bug, uncompress does not accept bytes
        with self.assertRaises(TypeError):
            zlib.decompress(b"foo")

        with self.assertRaises(TypeError):
            bz2.decompress(b"foo")

        with self.assertRaises(TypeError):
            lzma.decompress(b"foo")

if __name__ == "__main__":
    unittest.main()
