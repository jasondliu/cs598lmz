from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# The above BZ2Decompressor().decompress() call returns the following bytes:
# b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# The decompression algorithm used by bzip2 is a variation of the LZ77 algorithm.
# The LZ77 algorithm uses a sliding window during compression.
# The sliding window is of size W, where W is a parameter of the compression algorithm.
# A common value for W is 32 KB.
# The sliding window operates on a stream
