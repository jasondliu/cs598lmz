import bz2
# Test BZ2Decompressor.flush()

class TestBZ2(unittest.TestCase):

    def test_flush_eof_error(self):
        with bz2.open(TESTFN, 'wb') as compressor:
            compressor.write(b'hello')
        with bz2.open(TESTFN, 'rb') as decompressor:
            decompressor.read(1)
            self.assertRaises(EOFError, decompressor.flush)

    def test_flush_closed_error(self):
        with bz2.open(TESTFN, 'wb') as compressor:
            compressor.write(b'hello')
        with bz2.open(TESTFN, 'rb') as decompressor:
            decompressor.read(1)
            decompressor.close()
            self.assertRaises(ValueError, decompressor.flush)

    @bigmemtest(size=_2G + 10, memuse=1)
    def test_big_compressor_flush(self, size):
        # Issue #16444: crash when flushing compressor with large input
        with
