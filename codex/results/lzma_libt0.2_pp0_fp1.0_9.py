import lzma
lzma.LZMA_OK

#
# Test the LZMAFile class
#

class TestLZMAFile(unittest.TestCase):
    def test_read_eof(self):
        # Issue #17097: LZMAFile.read() should return an empty string
        # at EOF, not raise EOFError.
        with lzma.open(TESTFN, "wb") as f:
            f.write(b"test")
        with lzma.open(TESTFN, "rb") as f:
            self.assertEqual(f.read(), b"test")
            self.assertEqual(f.read(), b"")
            self.assertEqual(f.read(), b"")

    def test_read_eof_after_seek(self):
        # Issue #17097: LZMAFile.read() should return an empty string
        # at EOF, not raise EOFError.
        with lzma.open(TESTFN, "wb") as f:
            f.write(b"test
