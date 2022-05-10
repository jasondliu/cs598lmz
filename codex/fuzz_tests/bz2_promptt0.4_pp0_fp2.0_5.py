import bz2
# Test BZ2Decompressor.__init__()

def test_decompressor_init():
    bz2.BZ2Decompressor()

# Test BZ2Decompressor.decompress()

def test_decompressor_decompress():
    d = bz2.BZ2Decompressor()
    assert d.decompress(bz2.compress(b"foo")) == b"foo"

# Test BZ2Decompressor.decompress() with multiple calls

def test_decompressor_decompress_multiple():
    d = bz2.BZ2Decompressor()
    assert d.decompress(bz2.compress(b"foo")) == b"foo"
    assert d.decompress(bz2.compress(b"bar")) == b"bar"

# Test BZ2Decompressor.decompress() with multiple calls and unused data

def test_decompressor_decompress_multiple_unused():
    d = bz2.BZ2Decompressor()
    assert d.decomp
