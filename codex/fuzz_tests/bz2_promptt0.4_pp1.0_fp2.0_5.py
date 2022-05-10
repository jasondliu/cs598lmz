import bz2
# Test BZ2Decompressor

class TestBZ2Decompressor(unittest.TestCase):

    def test_decompress_eof(self):
        # check that an EOFError is raised when the compressed data does not
        # end with an EOF code
        decompressor = bz2.BZ2Decompressor()
        self.assertRaises(EOFError, decompressor.decompress,
                          b'BZh91AY&SY')

    def test_decompress_error(self):
        # check that a ValueError is raised when the compressed data stream
        # is corrupted
        decompressor = bz2.BZ2Decompressor()
        self.assertRaises(ValueError, decompressor.decompress,
                          b'BZh91AY&SY\x00\x00\x00\x00\x00\x00\x00\x00\x00')

    def test_decompress_non_block_boundary(self):
        # check that a ValueError is raised when the compressed data stream
        # does not end on a block boundary
