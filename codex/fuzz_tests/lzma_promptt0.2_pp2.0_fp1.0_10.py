import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    data = b"\x00" * 1000000
    compressed = lzma.compress(data)
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(compressed) == data
    assert decompressor.unused_data == b""
    assert decompressor.eof == True
    assert decompressor.decompress(b"garbage") == b""
    assert decompressor.unused_data == b"garbage"
    assert decompressor.eof == True
    assert decompressor.decompress(b"") == b""
    assert decompressor.unused_data == b"garbage"
    assert decompressor.eof == True
    # Test multiple decompress() calls
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(compressed[:1000]) == data[:1000]
    assert decompressor.unused_data == b""
    assert decompressor.eof == False
    assert decompressor
