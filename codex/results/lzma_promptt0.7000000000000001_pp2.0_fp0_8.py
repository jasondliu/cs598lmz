import lzma
# Test LZMADecompressor
def test_LZMADecompressor():
    data = b"x" * 10000
    comp = lzma.LZMACompressor()
    cdata = comp.compress(data)
    cdata += comp.flush()
    del comp
    comp = lzma.LZMADecompressor()
    udata = comp.decompress(cdata)
    udata += comp.flush()
    assert udata == data

# Test BZ2Compressor
def test_BZ2Compressor():
    data = b"x" * 10000
    comp = bz2.BZ2Compressor()
    cdata = comp.compress(data)
    cdata += comp.flush()
    del comp
    comp = bz2.BZ2Decompressor()
    udata = comp.decompress(cdata)
    udata += comp.flush()
    assert udata == data

# Test BZ2Decompressor
def test_BZ2Decompressor():
    data = b"x" * 10000
    comp = b
