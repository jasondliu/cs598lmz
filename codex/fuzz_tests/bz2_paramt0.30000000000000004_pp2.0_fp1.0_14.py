from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# bz2.BZ2Decompressor.decompress(data)
# Decompress data, returning uncompressed data as bytes.
# If you want to decompress data sequentially, use a BZ2Decompressor object and feed data to the decompress() method via repeated calls.

# bz2.BZ2Decompressor.unused_data
# The unconsumed portion of the compressed data.

# bz2.BZ2Decompressor.eof
# True if the end-of-stream marker has been reached.

# bz2.BZ2Decompressor.unconsumed_tail
# The unconsumed portion of the data passed to the decompress() method.

# bz2.BZ2Decompressor.decompress(data,
