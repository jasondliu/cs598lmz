import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    # Test LZMADecompressor with a file
    with lzma.open(TESTFN, "rb") as f:
        data = f.read()
    with lzma.open(TESTFN, "rb") as f:
        d = lzma.LZMADecompressor()
        data2 = d.decompress(f.read())
    assert data == data2

    # Test LZMADecompressor with a stream
    with lzma.open(TESTFN, "rb") as f:
        d = lzma.LZMADecompressor()
        data3 = b''
        while True:
            buf = f.read(1024)
            if not buf:
                break
            data3 += d.decompress(buf)
    assert data == data3

    # Test LZMADecompressor with a stream that is not a multiple of 1024
    with lzma.open(TESTFN, "rb") as f:
        d = l
