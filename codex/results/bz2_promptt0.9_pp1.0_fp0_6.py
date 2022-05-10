import bz2
# Test BZ2Decompressor.decompress() for various states.

b2_data = import_module('bz2').BZ2Compressor().compress(b'bzip2   compressed data')
b2_data_extra = b'extra data after the compressed data'

class TestBZ2Decompress:

    def test_decompress_basic(self):
        c = bz2.BZ2Decompressor()
        data = c.decompress(b2_data)
        eq(data, b'bzip2   compressed data')
        assert c.unused_data == b''
        assert c.eof
        assert not c.needs_input
        assert c.needs_input == c.eof

    def test_decompress_buffer(self):
        # Issue #33919: This used to trigger a TypeError with PyPy.
        bz2.decompress(bytearray(b2_data))

    def test_decompress_args(self):
        # Issue #36674: Previously, decompress required max_length to be
        # set
