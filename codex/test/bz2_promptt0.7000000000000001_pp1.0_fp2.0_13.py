import bz2
# Test BZ2Decompressor

def test_BZ2Decompressor_read():
    # Compress a binary file
    with open(support.TESTFN, "wb") as f:
        f.write(b"\0" * 100)
    with open(support.TESTFN, "rb") as f:
        c = f.read()
    with bz2.BZ2File(support.TESTFN2, "wb") as f:
        f.write(c)

    with open(support.TESTFN2, "rb") as f:
        d = bz2.BZ2Decompressor()
        # The magic number is part of the compressed data
        assert d.read(2) == b"BZ"
        assert f.read(2) == b"BZ"
        assert d.unused_data == b"BZ"
        assert f.read(2) == b"h1"
        # The unused data from the previous read is returned
        assert d.read(2) == b"h1"
