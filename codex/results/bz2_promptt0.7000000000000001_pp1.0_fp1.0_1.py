import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY\xd5\x8e\x1cD\x0a\x00\x00\x04\xe8\x02\xff\x85\x11\xc4\xbc\xc2\x00!\x10W(\xcf\xef\xe3\x0d\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
d = bz2.BZ2Decompressor()
result = []
for c in data:
    r = d.decompress(c)
    if r:
        result.append(r)
result = b''.join(result)
print(result)
# Test BZ2Decompressor with blocks
d = bz2.BZ2Decompressor()
result = []
for block in data:
    r = d.decompress(block)
    if r:
        result.append(r)
result =
