import bz2
# Test BZ2Decompressor
ct = b'BZh91AY&SY.\xd9\xa5\x80F\x1c\x00\xe0\xe8\x00\x00\x00\x00'
d = bz2.decompress(ct)
print(d)

# Test BZ2Compressor
c = bz2.compressor(ct)
print(c)

# Test iter
dc = bz2.decompressor(ct)
for chunk in iter(lambda: dc.read(30), b''):
    print(chunk)
