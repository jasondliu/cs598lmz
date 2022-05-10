from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

#  bz2.decompress(data)
#  bz2.decompress(data, max_length)

#  Decompress data, returning uncompressed data as bytes.
#  If the max_length parameter is specified then the return value will be no longer than max_length.
#  If the data is not compressed or decompression fails, a ValueError is raised.

#  data: bytes-like object
#  max_length: int
#  Returns: bytes

#  class bz2.BZ2Decompressor
#  New in version 3.3.

#  This class provides a decompression object to decompress data incrementally.

#  decompress(data, max_length=-1)
#  Decompress data,
