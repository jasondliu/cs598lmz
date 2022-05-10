from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# The BZIP2 file format is documented at https://en.wikipedia.org/wiki/Bzip2#File_format
# It is an extension of the DEFLATE format, and the decompressor can be found in the zlib module.
# The first few bytes of the compressed data are metadata and not compressed at all.
# The first byte indicates the compression level and whether a randomisation preprocessing step was used.
# The
