import lzma
# Test LZMADecompressor against the test vectors in RFC 1951

def test_empty_decompressor():
    # Test a decompressor initialized with no data
    d = lzma.LZMADecompressor()
    assert d.decompress(b'') == b''
    assert d.unused_data == b''
    assert d.eof is False
    with pytest.raises(EOFError):
        d.decompress(b'x')

def test_one_byte_at_a_time():
    # Test decompressing one byte at a time
    compressed = (
        b'\x5d\x00\x00\xff\xff\x07\xc0\x04\x60\x00'
        b'\x08\x04\x00\x01\x00\x00\x00\x01\x66\x6f\x6f'
        b'\x62\x61\x72'
    )

    d = lzma.LZMADecompressor()
    assert d.decompress(compressed[
