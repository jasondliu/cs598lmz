import lzma
# Test LZMADecompressor.flush()

def test_flush():
    dec = lzma.LZMADecompressor()
    assert dec.flush() == b''
    dec.decompress(b'\x00')
    assert dec.flush() == b''
    data = bytes(range(1, 257))
    assert dec.decompress(data) == data
    assert dec.flush() == b''
    assert dec.decompress(lzma.LZMACompressor().compress(b'a' * 1024)) == b'a' * 1024
    assert dec.flush() == b''
    assert dec.decompress(b'\x00') == b''
    assert dec.flush() == b''
    data += bytes(range(1, 257))
    assert dec.decompress(data) == data
    assert dec.flush() == b''
