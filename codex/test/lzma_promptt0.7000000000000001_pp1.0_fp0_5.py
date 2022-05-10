import lzma
# Test LZMADecompressor

def test():
    data = b"a" * 10000
    cdata = lzma.compress(data)
    decomp = lzma.LZMADecompressor()
    assert decomp.decompress(cdata) == data
    cdata += lzma.compress(b"b" * 1000)
    assert decomp.decompress(cdata, max_length=11000) == data + b"b" * 1000
    assert decomp.unused_data == lzma.compress(b"b" * 1000)
    # Check that we can chain another LZMADecompressor after this one
    ndata = decomp.decompress(b"")
    ndecomp = lzma.LZMADecompressor()
    assert ndecomp.decompress(ndata) == data + b"b" * 1000

