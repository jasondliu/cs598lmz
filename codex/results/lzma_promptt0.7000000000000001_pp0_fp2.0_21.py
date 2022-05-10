import lzma
# Test LZMADecompressor.copy

def test_copy():
    def gen():
        d = lzma.LZMADecompressor()
        yield d.decompress(b'\x00')
        yield d.decompress(b'\x00')
        yield d.decompress(b'\x00')
        raise lzma.LZMAError(1)

    f = gen()
    d1 = lzma.LZMADecompressor()
    try:
        next(f)
    except lzma.LZMAError:
        d2 = d1.copy()
    try:
        next(f)
    except lzma.LZMAError:
        d3 = d2.copy()
    try:
        next(f)
    except lzma.LZMAError:
        d4 = d3.copy()
    try:
        next(f)
    except lzma.LZMAError:
        pass
    else:
        assert False, "Exception not raised"
    assert d1.decompress
