import lzma
# Test LZMADecompressor and LZMACompressor
def test_lzma():
    data = b'\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01'
    comp = lzma.compress(data)
    uncomp = lzma.decompress(comp)
    assert data == uncomp

# Test lzma.open()
def test_open():
    data = b'\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01'
    with lzma.open(test.support.TESTFN, "wb") as f:
        f.write(data)
    with lzma.open(test.support.TESTFN, "rb") as f:
        uncomp = f.read()
    assert data == uncomp
    os.remove(test.support.TESTFN)

