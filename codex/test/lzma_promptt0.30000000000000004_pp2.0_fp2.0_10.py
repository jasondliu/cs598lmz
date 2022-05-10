import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    c = lzma.LZMADecompressor()
    assert c.decompress(b"") == b""

    c = lzma.LZMADecompressor()
    assert c.decompress(b"\x00") == b"\x00"

    c = lzma.LZMADecompressor()
    assert c.decompress(b"\x00\x00") == b"\x00\x00"

    c = lzma.LZMADecompressor()
    assert c.decompress(b"\x00\x00\x00") == b"\x00\x00\x00"

    c = lzma.LZMADecompressor()
    assert c.decompress(b"\x00\x00\x00\x00") == b"\x00\x00\x00\x00"

    c = lzma.LZMADecompressor()
    assert c.decompress
