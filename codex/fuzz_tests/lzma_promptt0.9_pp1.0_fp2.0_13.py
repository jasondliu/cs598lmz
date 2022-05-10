import lzma
# Test LZMADecompressor against the reference implementation in C.
# The simple test cases are taken from the Python reference docs. They
# are tested both as individual updates and all together.
class TestLZMADecompressor(unittest.TestCase):
    def test_decompressor(self):
        c = lzma.LZMADecompressor()
        self.assertFalse(c.eof)
        self.assertEqual(b"", c.decompress(b""))
        with self.assertRaisesRegex(lzma.LZMAError, "invalid input"):
            c.decompress(b"foo")
        self.assertFalse(c.eof)
        self.assertEqual(
            b"",
            c.decompress(b"\x00\x00\x00\x00\x00\x04\x00\xff\xff"),
        )
        self.assertFalse(c.eof)
        self.assertEqual(b"foo", c.decompress(b"foo\x00\x00\x00\
