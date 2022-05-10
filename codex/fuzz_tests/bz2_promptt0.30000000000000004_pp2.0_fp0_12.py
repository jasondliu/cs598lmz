import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
with open('data/sample.bz2', 'rb') as f:
    data = f.read()
    print(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'r') as f:
    print(f.read())

# Test bz2.compress()

print(bz2.compress(b'Hello, world!'))

# Test bz2.decompress()

print(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))
