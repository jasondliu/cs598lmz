import lzma
# Test LZMADecompressor.decompress()

# Test decompression of a file with a single chunk
with lzma.open(TESTFN, "wb") as f:
    f.write(b"foo")
with lzma.open(TESTFN, "rb") as f:
    data = f.read()
    d = lzma.LZMADecompressor()
    data2 = d.decompress(data)
    data2 += d.decompress(b"")
    data2 += d.decompress(b"", True)
    assert data2 == b"foo"

# Test decompression of a file with multiple chunks
with lzma.open(TESTFN, "wb") as f:
    f.write(b"foo")
    f.write(b"bar")
with lzma.open(TESTFN, "rb") as f:
    data = f.read()
    d = lzma.LZMADecompressor()
    data2 = d.decompress(data)
    data2 += d.decompress
