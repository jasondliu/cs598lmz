import lzma
# Test LZMADecompressor
class TestLZMADecompressor(unittest.TestCase):
    def test_read1(self):
        comp = lzma.LZMADecompressor()
        self.assertRaises(EOFError, comp.read, 1)
    def test_read2(self):
        comp = lzma.LZMADecompressor()
        comp.decompress(b'\x00')
        self.assertEqual(comp.unused_data, b'\x00')
        self.assertRaises(EOFError, comp.read, 1)
    def test_read3(self):
        comp = lzma.LZMADecompressor()
        comp.decompress(b'x')
        self.assertEqual(comp.unused_data, b'x')
        self.assertEqual(comp.read(1), b'x')
        self.assertEqual(comp.unused_data, b'')
    def test_read4(self):
        comp = lzma.LZMAD
