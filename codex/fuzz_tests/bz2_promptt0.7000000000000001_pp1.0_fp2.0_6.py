import bz2
# Test BZ2Decompressor and BZ2Compressor

data = b"1234567890" * 100000
compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# Feeding bytes to the compressor returns blocks of compressed data,
# which may be empty until it has enough data for a full compressed
# block.
compressed_data = b"".join(compressor.compress(data))
compressed_data += compressor.flush()

# Decompress accepts the compressed data one chunk at a time,
# decompressing a chunk at a time.
decompressed_data = b""
while compressed_data:
    chunk = compressed_data[:1024]
    compressed_data = compressed_data[1024:]
    decompressed_data += decompressor.decompress(chunk)

# The decompressor's unused_data attribute contains any data that the
# decompressor was unable to decompress because it was missing data
# from previous chunks.
decompressed_data += decompressor.decompress(decompressor.unused_data)
decomp
