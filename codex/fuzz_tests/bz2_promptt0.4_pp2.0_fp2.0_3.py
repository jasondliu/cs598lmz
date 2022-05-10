import bz2
# Test BZ2Decompressor

def test_BZ2Decompressor():
    with bz2.BZ2File(test_support.findfile("test1.bz2"), "rb") as f:
        decomp = bz2.BZ2Decompressor()
        data = f.read(50)
        more = decomp.decompress(data)
        more += decomp.decompress(f.read())
        more += decomp.flush()
        assert more == open(test_support.findfile("test1"), "rb").read()

# Test BZ2Compressor

def test_BZ2Compressor():
    with bz2.BZ2File(test_support.findfile("test1.bz2"), "rb") as f:
        data = f.read()
    with bz2.BZ2File(test_support.TESTFN, "wb", compresslevel=9) as f:
        comp = bz2.BZ2Compressor(9)
        f.write(comp.compress(data))
        f.write(comp.flush())

