import bz2
# Test BZ2Decompressor.decompress README example.

# Number of characters is a multiple of 1024.
data = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

print('Python', data)
assert data == b'Python'

# Number of characters is not a multiple of 1024.
data = bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

print('Hello', data)
assert data == b'Hello'

# Number of characters is less than 1024.
data = bz2.
