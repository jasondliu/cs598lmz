import bz2
# Test BZ2Decompressor

data = bz2.compress(bytes(range(256)))

# Create a decoder object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
decompressor.decompress(data)

# Decompress the data, and return the chunk size
decompressor.decompress(data, 1024)

# Decompress the data and return the chunk size
decompressor.decompress(data, 8192)

# Decompress the data and return the chunk size
decompressor.decompress(data, 0)

# Finalise decompression
decompressor.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Decompress the data
decompressor.decompress(data)


