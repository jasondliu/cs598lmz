import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SY\xc4\x98\xc4\x81\x11\x00\x00\x00\x00\x00\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test BZ2File
with bz2.BZ2File('example.bz2', 'wb') as f:
    f.write(b'hello world!hello world!hello world!hello world!')
with bz2.BZ2File('example.bz2', 'rb') as f:
    print(f.read())

# Test compress and decompress
data = b'hello world!hello world!hello world!hello world!'
compressed = bz2.compress(data)
decompressed = bz2.decompress(compressed)
print(len(data),
