import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(TESTFN, "rb") as f:
        data = f.read()
    with lzma.open(TESTFN, "rb") as f:
        f.seek(0)
        d = lzma.LZMADecompressor()
        data1 = d.decompress(f.read())
    assert data == data1

# Test LZMADecompressor.decompress()

def test_lzma_decompressor_decompress():
    with lzma.open(TESTFN, "rb") as f:
        data = f.read()
    with lzma.open(TESTFN, "rb") as f:
        f.seek(0)
        d = lzma.LZMADecompressor()
        data1 = b""
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            data1 += d.decompress(chunk)
