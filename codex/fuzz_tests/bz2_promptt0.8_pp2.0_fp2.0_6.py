import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
a = decomp.decompress(compressed)
assert a == uncompressed
a = decomp.decompress(compressed[:100])
assert not a
a = decomp.decompress(compressed[100:])
assert a == uncompressed[100:]
decomp = bz2.BZ2Decompressor()
a = decomp.decompress(compressed)
assert a == uncompressed
# Test incremental BZ2Decompressor
decomp = bz2.BZ2Decompressor()
res = []
for i in range(0, len(compressed), 10):
    res.append(decomp.decompress(compressed[i:i+10]))
assert b''.join(res) == uncompressed
# Test BZ2File
bz2file = bz2.BZ2File(io.BytesIO(compressed))
assert bz2file.read() == uncompressed
bz2file = bz2.BZ2File(io.BytesIO(compressed[:100]))
