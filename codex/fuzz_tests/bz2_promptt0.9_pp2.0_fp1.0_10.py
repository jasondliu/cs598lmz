import bz2
# Test BZ2Decompressor with extra len and memoryview
with open('testdata/sample.tar', 'rb') as f, \
     bz2.BZ2Decompressor(5) as c:
    data = f.read()
    mv = memoryview(data)
    mv_len = len(mv)
    assert c.decompress(mv) == data

with open('testdata/sample.tar', 'rb') as f, \
     bz2.BZ2Decompressor() as c:
    data = f.read()
    mv = memoryview(data)
    mv_len = len(mv)
    assert c.decompress(mv) == data

# Test BZ2Compressor with extra len and memoryview
with open('testdata/sample.tar', 'rb') as f, \
     bz2.BZ2Compressor() as c:
    data = f.read()
    cdata = c.compress(data)
    cdata += c.flush()
    mv = memoryview(data)
    mv
