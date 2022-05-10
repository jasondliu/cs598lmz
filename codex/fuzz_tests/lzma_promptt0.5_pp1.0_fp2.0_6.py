import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    cdata = lzma.compress(b"foo")

    d = lzma.LZMADecompressor()
    data = d.decompress(cdata)
    assert data == b"foo"

    # Decompress again, with more data
    data = d.decompress(cdata)
    assert data == b"foo"

    # Decompress again, with more data
    data = d.decompress(cdata)
    assert data == b"foo"

    # Decompress again, with more data
    data = d.decompress(cdata)
    assert data == b"foo"

    # Decompress again, with more data
    data = d.decompress(cdata)
    assert data == b"foo"

    # Decompress again, with more data
    data = d.decompress(cdata)
    assert data == b"foo"

    # Decompress again, with more data
    data = d.decompress(cdata)
