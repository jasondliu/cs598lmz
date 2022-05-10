from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.BZ2Decompressor.decompress(data)

# decompress(data)
# Decompress data, returning uncompressed data as bytes.

# If you know the uncompressed size, you may specify it to avoid having to buffer the entire output file.

# Some formats, including ZIP and GZIP, can store a file without knowing the uncompressed size.

# In this case, the size argument should be zero.

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# bz2_decompressor = BZ2Decompressor()
# next_data = bz2_decompressor.decompress(bz2_data)
# print(next_data)

