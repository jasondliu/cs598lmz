import lzma
# Test LZMADecompressor

def test_lzma_decompressor_init():
    decompressor = lzma.LZMADecompressor()
    assert decompressor.eof is False
    assert decompressor.unused_data == b""
    assert decompressor.decompress(b"") == b""
    assert decompressor.unused_data == b""
    assert decompressor.eof is False
    assert decompressor.decompress(b"") == b""
    assert decompressor.unused_data == b""
    assert decompressor.eof is False
    assert decompressor.decompress(b"") == b""
    assert decompressor.unused_data == b""
    assert decompressor.eof is False
    assert decompressor.decompress(b"") == b""
    assert decompressor.unused_data == b""
    assert decompressor.eof is False
    assert decompressor.decompress(b"") == b""
    assert decompressor.unused_data == b""
    assert decompressor.eof is False
