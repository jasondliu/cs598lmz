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
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1)
        data += f.read1(1
