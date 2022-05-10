from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress all data
LZMADecompressor().decompress(data, max_length=None)

# decompress all data with a maximum length of 100 bytes
LZMADecompressor().decompress(data, max_length=100)

# decompress data in chunks
d = LZMADecompressor()
d.decompress(data1)
d.decompress(data2)
d.decompress(data3)
d.flush()

# decompress data in chunks with a maximum length of 100 bytes
d = LZMADecompressor()
d.decompress(data1, max_length=100)
d.decompress(data2, max_length=100)
d.decompress(data3, max_length=100)
d.flush()

# decompress data in chunks with a maximum length of 100 bytes,
# and check that the decompressed data is valid
d = LZMADecompressor()
d.decompress(data1, max_length=100
