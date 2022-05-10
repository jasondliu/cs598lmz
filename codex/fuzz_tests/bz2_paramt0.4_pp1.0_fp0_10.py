from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\xc4\x98\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# The decompress() method can take an optional max_length argument, which is the maximum number of bytes to return.
# If the compressed data is longer than this, only the first max_length bytes of the decompressed data will be returned,
# and the rest discarded.
# This can be used to decompress a chunk of data at a time.

# The decompress() method also accepts optional args, which should be a dictionary of keyword arguments.
# One of these is the wbits argument, which represents the window size used when compressing the data.
# This value must be supplied when decompressing, and must be the same as the wbits value used to compress the data.
# If it is not, decompress() will raise an error.

# The decompress() method can be used in a for loop.
# This
