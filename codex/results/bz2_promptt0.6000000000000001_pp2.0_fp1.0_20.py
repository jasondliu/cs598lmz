import bz2
# Test BZ2Decompressor
# https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor
# https://docs.python.org/3/library/bz2.html#bz2.decompress

data = b'BZh91AY&SY.\xc8N\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(data)
decompressed_data

# This is what the original data should look like
'BZh91AY&SY\xe2\x96\x8b\xe2\x96\x91\xe2\x96\xbc\x17\xfc\x84\
