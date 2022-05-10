import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?\xe7\xff\xe00\x01\x99\xaa\x00\xc0#\x0e\xfd\x01\n\x00\x00\x00'
d = bz2.BZ2Decompressor()
print(d.decompress(data))
print(d.unused_data)

# Test BZ2Compressor
c = bz2.BZ2Compressor()
print(c.compress(b"foo"))
print(c.flush())

# Test BZ2File
with bz2.BZ2File('/tmp/foo.bz2', 'w') as f:
    f.write(b"foo")

