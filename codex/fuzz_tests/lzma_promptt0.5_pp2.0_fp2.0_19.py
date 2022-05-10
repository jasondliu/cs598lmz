import lzma
# Test LZMADecompressor.format

with lzma.open(TESTFN, "w") as f:
    f.write(b"foo")

with lzma.open(TESTFN) as f:
    assert f.format == lzma.FORMAT_XZ

with lzma.open(TESTFN, format=lzma.FORMAT_AUTO) as f:
    assert f.format == lzma.FORMAT_XZ

with lzma.open(TESTFN, format=lzma.FORMAT_XZ) as f:
    assert f.format == lzma.FORMAT_XZ

with lzma.open(TESTFN, format=lzma.FORMAT_ALONE) as f:
    assert f.format == lzma.FORMAT_ALONE

with lzma.open(TESTFN, format=lzma.FORMAT_RAW) as f:
    assert f.format == lzma.FORMAT_RAW

with lzma.open(TESTFN, format=lzma.
