import lzma
# Test LZMADecompressor.
for size in [0, 1, 7, 8, 9, 15, 16, 17, 100]:
    data = b'x' * size
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
    with support.captured_stdout() as out:
        d.decompress(cdata)
    with support.captured_stdout() as out:
        d.flush()
    support.unlink(support.TESTFN)

# Test decompressing a truncated file
with open(support.TESTFN, "wb") as f:
    f.write(lzma.compress(b"hello world"))
with open(support.TESTFN, "rb") as f:
    f.truncate(10)
with open(support.TESTFN, "rb") as f:
    data = f.read()
    with pytest.raises(lzma.LZMAError) as cm:
        lzma.decompress(data)
    assert cm.value.
