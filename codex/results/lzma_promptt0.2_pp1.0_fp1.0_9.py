import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(TESTFN, "w") as f:
        f.write(b"foo")
    with lzma.open(TESTFN, "r") as f:
        assert f.read() == b"foo"
    with lzma.open(TESTFN, "rb") as f:
        assert f.read() == b"foo"
    with lzma.open(TESTFN, "rt") as f:
        assert f.read() == "foo"
    with lzma.open(TESTFN, "rt", encoding="utf-8") as f:
        assert f.read() == "foo"
    with lzma.open(TESTFN, "rt", encoding="latin-1") as f:
        assert f.read() == "foo"
    with lzma.open(TESTFN, "rt", newline="") as f:
        assert f.read() == "foo"
    with lzma.open(TESTFN, "rt
