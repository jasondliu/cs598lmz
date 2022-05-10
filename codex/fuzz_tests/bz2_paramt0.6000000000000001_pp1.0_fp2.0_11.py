from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# Lets try to decompress some data
# encoded with BZIP2 compression
# We will use the same data from the previous example

# uncompressed data
uncompressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

# compressed data
compressed_data = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# use the bz2 module
import bz2

# bz2.decompress(compressed_data)
# b'BZh91AY&
