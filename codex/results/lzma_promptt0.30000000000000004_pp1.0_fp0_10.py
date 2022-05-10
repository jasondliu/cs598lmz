import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with lzma.open(TESTFN, "rb") as f:
        data = f.read()
    assert data == DATA


def test_lzma_decompressor_read1():
    with lzma.open(TESTFN, "rb") as f:
        data = f.read1(1)
        data += f.read1(1)
        data += f.read1(1000)
    assert data == DATA


def test_lzma_decompressor_readinto():
    buf = bytearray(len(DATA))
    with lzma.open(TESTFN, "rb") as f:
        n = f.readinto(buf)
    assert n == len(DATA)
    assert buf == DATA


def test_lzma_decompressor_readinto1():
    buf = bytearray(1)
    with lzma.open(TESTFN, "rb") as f:
        n = f.readinto1(buf)
        assert
