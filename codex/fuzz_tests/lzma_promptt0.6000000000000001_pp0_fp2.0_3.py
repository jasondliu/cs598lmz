import lzma
# Test LZMADecompressor

def test_lzma_decompressor_no_check():
    data = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    decomp = lzma.LZMADecompressor()
    assert decomp.decompress(data) == b""
    assert decomp.unused_data == b""
    assert decomp.eof

def test_lzma_decompressor_check_crc32():
    data = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    decomp = lzma.LZMADecompressor(format=lzma.FORMAT_XZ, check=-1)
    assert decomp.decompress(data) == b""
    assert decomp.unused_data == b""
    assert
