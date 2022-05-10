from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 'The quick brown fox jumps over the lazy dog.'

# Compress the data
data = LZMACompressor().compress(data) + LZMACompressor().flush()

# Decompress the data
LZMADecompressor().decompress(data)

# 'The quick brown fox jumps over the lazy dog.'

# Compress the data
compressor = LZMACompressor()
chunks = []
for chunk in data_chunks:
    chunks.append(compressor.compress(chunk))
chunks.append(compressor.flush())

# Decompress the data
decompressor = LZMADecompressor()
chunks = []
for chunk in data_chunks:
    chunks.append(decompressor.decompress(chunk))
''.join(chunks)

# 'The quick brown fox jumps over the lazy dog.'

# Compress the data
compressor = LZMACompressor()
with open('compressed.xz', 'wb') as f:
    for chunk in
