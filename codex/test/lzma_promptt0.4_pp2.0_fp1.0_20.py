import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    lzc = lzma.LZMADecompressor()
    assert lzc.decompress(b"") == b""
    assert lzc.unused_data == b""
    assert lzc.eof is False
    lzc.decompress(b"\x00")
    assert lzc.unused_data == b"\x00"
    assert lzc.eof is False
    lzc.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00")
    assert lzc.unused_data == b"\x00\x00\x00\x00\x00\x00\x00\x00"
    assert lzc.eof is False
    lzc.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    assert lzc.unused_data
