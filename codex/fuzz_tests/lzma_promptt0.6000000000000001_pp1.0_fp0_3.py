import lzma
# Test LZMADecompressor.decompress() in byte mode
# and LZMADecompressor.decompress() in text mode
# with LZMAError exceptions.

def test_decompress_byte_mode_exceptions():
    # LZMAError must be raised when the compressed data is truncated.
    dc = lzma.LZMADecompressor()
    with pytest.raises(lzma.LZMAError):
        dc.decompress(b'\x00')
    # LZMAError must be raised when the compressed data length is invalid.
    with pytest.raises(lzma.LZMAError):
        dc.decompress(b'\xff' + b'\x00' * 4 + b'\x00')
    # LZMAError must be raised when the compressed data is corrupted.
    with pytest.raises(lzma.LZMAError):
        dc.decompress(b'\xff' + b'\x00' * 4 + b'\x00' * 4)
    # LZMAError
