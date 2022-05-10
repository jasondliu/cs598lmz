import bz2
# Test BZ2Decompressor on an empty file
bz2_decompressor = bz2.BZ2Decompressor()
bz2_decompressor.decompress(b'')

# Test BZ2Decompressor on a file with no compressed data
bz2_decompressor.decompress(b'foo')

# Test BZ2Decompressor on a file with some compressed data
bz2_decompressor.decompress(b'BZh91AY&SY\xc4\x8d\x06\x00\x00\x00\x81\x04$')

# Test BZ2Decompressor on a file with some more compressed data
bz2_decompressor.decompress(b'\x00\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
