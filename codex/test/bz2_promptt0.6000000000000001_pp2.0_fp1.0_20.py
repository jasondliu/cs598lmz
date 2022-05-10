import bz2
# Test BZ2Decompressor
# https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor
# https://docs.python.org/3/library/bz2.html#bz2.decompress

data = b'BZh91AY&SY.\xc8N\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
decompressor = bz2.BZ2Decompressor()
