from bz2 import BZ2Decompressor
BZ2Decompressor(bufsize=0).decompress(start)

# Output #
# 'BZh91AY&SY'

# The file contains only the compressed data from the first
# BZIP2 block. The first 10 bytes are the 2-byte sequence that
# identifies the block as being compressed with BZIP2 ('BZh')
# followed by a single-byte block header ('9'), the block size
# ('1A'), the randomisation parameter ('Y'), and the block checksum ('&' and 'SY').

# The 9-byte block header is decoded as follows:

#     1 byte : block size (number of 100k elements) - 1
#     1 byte : randomisation parameter
#     1 byte : block checksum: 0-255 =&gt; CRC-24Q
#     3 bytes : block compressed size (in bytes) - 1
#     4 bytes : block uncompressed size (in bytes) - 1

# The checksum is not verified for this example. The first
# byte of the block header has a value of '1A', in hexadecimal,
# which corresponds to the decimal
