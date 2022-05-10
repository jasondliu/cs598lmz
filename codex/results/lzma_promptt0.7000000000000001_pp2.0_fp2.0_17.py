import lzma
# Test LZMADecompressor.decompress()'s handling of the
# BUFFER_ERROR condition.
class MyDecompressor(lzma.LZMADecompressor):
    def decompress(self, data, max_length=None):
        tmp = super().decompress(data, max_length)
        # Use up all the internal buffer
        super().decompress(b'', 1)
        # Force the next decompress() call to raise BUFFER_ERROR.
        super().decompress(b'x' * 100, 1)
        return tmp

def test_decompress_buffer_error():
    dec = MyDecompressor()
    with pytest.raises(lzma.LZMAError) as excinfo:
        dec.decompress(b'x' * 100)
    assert excinfo.value.errno == lzma.LZMA_BUF_ERROR

def test_decompress_buffer_error_with_max_length():
    dec = MyDecompressor()
    with pytest.raises(lzma.LZMAError
