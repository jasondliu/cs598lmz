import bz2
# Test BZ2Decompressor with a BZ2Decompressor object

data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'
d = bz2.BZ2Decompressor()
result = []
for c in data:
    r = d.decompress(bytes([c]))
    if r:
        result.append(r)
result = b''.join(result)
result

# Test BZ2Decompressor with a decompress() call

data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'
