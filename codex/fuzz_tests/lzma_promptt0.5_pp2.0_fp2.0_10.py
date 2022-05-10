import lzma
# Test LZMADecompressor.read()

class LZMADecompressorTest(unittest.TestCase):

    def test_read_basic(self):
        data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00'
        c = lzma.LZMADecompressor()
        self.assertEqual(c.read(1), b'')
        self.assertEqual(c.read(100), b'hello world!')
        self.assertEqual(c.read(1), b'')
        self.assertEqual(c.unused_data, b'')

    def test_read_after_eof(self):
        data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\
