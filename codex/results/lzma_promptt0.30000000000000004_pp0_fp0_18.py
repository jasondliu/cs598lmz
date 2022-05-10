import lzma
# Test LZMADecompressor

# Test that it works as a context manager
with lzma.LZMADecompressor() as dec:
    assert dec.eof is False
    assert dec.unused_data == b""
    assert dec.decompress(b"") == b""
    assert dec.unused_data == b""
    assert dec.eof is False
    assert dec.decompress(b"\x00") == b""
    assert dec.unused_data == b"\x00"
    assert dec.eof is False
    assert dec.decompress(b"\x00") == b""
    assert dec.unused_data == b"\x00"
    assert dec.eof is False
    assert dec.decompress(b"\x00") == b""
    assert dec.unused_data == b"\x00"
    assert dec.eof is False
    assert dec.decompress(b"\x00") == b""
    assert dec.unused_data == b"\x00"
    assert dec.eof is
