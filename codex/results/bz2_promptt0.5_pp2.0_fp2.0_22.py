import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test BZ2File
f = bz2.BZ2File(BytesIO(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))
f.read()


# Test BZ2File with mode 'w'.
f = bz2.BZ2File(BytesIO(), mode='w')
f.write(b'hello world')
f.close()

f = bz2.BZ2File(BytesIO(), mode='wb')
f.write
