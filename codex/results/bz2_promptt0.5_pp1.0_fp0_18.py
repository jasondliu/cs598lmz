import bz2
# Test BZ2Decompressor.readinto()

# Read from a file
data = b'BZh91AY&SY.\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
c = bz2.BZ2Decompressor()
with open('test.bz2', 'wb') as f:
    f.write(data)

with open('test.bz2', 'rb') as f:
    c.decompress(f.read())

with open('test.bz2', 'rb') as f:
    c.decompress(f.read())

with open('test.bz2', 'rb') as f:
    c.decompress(f.read())

with open('test.bz2', 'rb') as f:
    c.decomp
