import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() takes a byte string and returns a byte string
# bz2.decompress() takes a byte string and returns a byte string

# bz2.BZ2Compressor and bz2.BZ2Decompressor are used for streaming compression
# and decompression

# Compress data in one chunk
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(b'Hello World!')
compressed_data += compressor.flush()

# Compress data in chunks
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(b'Hello ')
compressed_data += compressor.compress(b'World!')
compressed_data += compressor.flush()

# Decompress data in one chunk
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)

# Decompress data
