import lzma
lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xca\xccK(I\xcdI\x01\x00\x00\x00\x04\x00\x00\x00\x00')

# Compression

import bz2
bz2.compress(b'hello world!')

# Decompression

import bz2
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Compression

import zlib
zlib.compress(b'hello world!')

# Decompression

import zlib
zlib.decomp
