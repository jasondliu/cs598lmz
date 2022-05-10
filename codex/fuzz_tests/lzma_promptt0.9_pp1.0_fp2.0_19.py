import lzma
# Test LZMADecompressor class with file interface

def get_filename(name):
    return os.path.join(os.path.dirname(__file__), "support", name)

def test_eof():
    dec = lzma.LZMADecompressor()
    data = dec.unconsumed_tail
    assert not dec.eof
    raw = b"inflated"
    for b in raw[:-1]:
        data += dec.decompress(b)
    data += dec.decompress(raw[-1:])
    assert not dec.eof
    assert dec.unused_data == b""
    assert dec.unconsumed_tail == b""
    data += dec.decompress(dec.eof)
    assert dec.eof
    assert dec.unused_data == b""
    assert dec.unconsumed_tail == b""

def test_decompress():
    dec = lzma.LZMADecompressor()
    fname = get_filename("lzma_corrupt.xz")

    with
