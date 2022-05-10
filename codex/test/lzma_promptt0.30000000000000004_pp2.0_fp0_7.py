import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    # Test the decompressor with a single-chunk stream.
    with open(TESTFN, "wb") as f:
        f.write(b"foo" * 100000)
    with open(TESTFN, "rb") as f:
        compressed = lzma.compress(f.read())
    d = lzma.LZMADecompressor()
    assert d.decompress(compressed) == b"foo" * 100000

    # Test the decompressor with a multi-chunk stream.
    with open(TESTFN, "wb") as f:
        f.write(b"foo" * 100000)
    with open(TESTFN, "rb") as f:
        compressed = lzma.compress(f.read())
    d = lzma.LZMADecompressor()
    chunks = []
