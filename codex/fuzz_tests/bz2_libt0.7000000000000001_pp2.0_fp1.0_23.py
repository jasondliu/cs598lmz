import bz2
bz2.BZ2Compressor(compresslevel=9)

# decompress
bz2.BZ2Decompressor()

# the bz2 module has a function to compress data
s = b'witch which has which witches wrist watch'
len(s)

t = bz2.compress(s)
len(t)

# decompress
bz2.decompress(t)

# the zlib module is another popular lossless compression library
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

# decompress
zlib.decompress(t)
zlib.crc32(s)
