import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Decompress a random string
    data = b'\x00' * 4 + lzma.LZMACompressor().compress(b'random data')
    lz = lzma.LZMADecompressor()
    assert lz.decompress(data) == b'random data'
    assert lz.unused_data == b''
    # Try decompressing from a file
    with open(TESTFN, "wb") as f:
        f.write(data)
    with open(TESTFN, "rb") as f:
        assert lz.decompress(f.read()) == b'random data'
    assert lz.unused_data == b''
    # Try decompressing from a file-like object
    with open(TESTFN, "wb") as f:
        f.write(data)
    with open(TESTFN, "rb") as f:
        assert lz.decompress(f) == b'random data'
    assert lz.un
