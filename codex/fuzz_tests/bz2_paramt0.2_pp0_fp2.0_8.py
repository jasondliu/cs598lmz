from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Compress data
data = b'We are the knights who say Ni!'
compressor = BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Compress data with context manager
with BZ2Compressor() as compressor:
    for line in data:
        compressor.compress(line)
    compressed_data = compressor.flush()

# Decompress data with context manager
with BZ2Decompressor() as decompressor:
    for chunk in chunks:
        decompressed_data.append(decompressor.decompress(chunk))
    remaining_data = decompressor.flush()
