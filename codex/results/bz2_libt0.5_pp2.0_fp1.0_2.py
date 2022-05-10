import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# The above is the output of bz2.compress(data)

# Since the bz2 compression algorithm is deterministic, the same data will result in the same compressed data

# Compression level is an integer from 1 to 9, with 9 being the highest compression level

# Compression level 1 is the fastest, but the compression ratio is not very good

# Compression level 9 is the slowest, but the compression ratio is the best

# If no compression level is specified, the default is 9

# The bz2 module includes the compress() and decompress() functions for compressing and decompressing data

# The compress() function takes in a string of data and returns a compressed string

# The decompress() function takes in a compressed string and
