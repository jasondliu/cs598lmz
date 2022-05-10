import lzma
# Test LZMADecompressor read method
def test_read():
    dec = lzma.LZMADecompressor()

    data = b"\x00\x00\x00\x00"
    assert dec.read(100) == b""
    assert dec.unconsumed_tail is None

    dec.decompress(data)
    assert dec.read(100) == b""
    assert dec.unconsumed_tail is None

    data = (
        b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00"
        b"\x01\x00\x00\x00\x00\x00\x00\x00"
    )
    expected = (b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    assert dec.read(100) == expected
    assert dec.unconsumed_tail
