from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Compress data
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.compress(data)

# Compress data using compresslevel
bz2.compress(data, compresslevel=9)

# Compress data using compresslevel and return the size of the compressed data
bz2.compress(data, compresslevel=9)
len(bz2.compress(data, compresslevel=9))

# Compress data using compresslevel and return the size of the compressed data
bz2.compress(data, compresslevel=9)
len(bz2.compress(data, compresslevel=9))

# Create a BZ2Compressor object
compressor = bz2.BZ2Comp
