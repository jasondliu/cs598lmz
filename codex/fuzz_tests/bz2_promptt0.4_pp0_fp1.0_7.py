import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'
compressor = bz2.BZ2Compressor()
ret = compressor.compress(data)
ret += compressor.flush()
print(ret)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(ret))

# Test BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(data)

with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read())
