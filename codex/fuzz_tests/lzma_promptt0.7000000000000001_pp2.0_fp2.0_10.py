import lzma
# Test LZMADecompressor in streaming mode

# Source data contains a short string of ASCII text
data = b"This is a test. This is only a test."

# Create a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Decompress data in chunks, returning uncompressed data as chunks
for chunk in iter(lambda: f.read(32 * 1024), b''):
    data += decompressor.decompress(chunk)
# Decompress the remaining data, returning the uncompressed data
data += decompressor.unconsumed_tail

# Release the (memory of the) decompressor
decompressor.flush()

print("Decompressed", len(data), "bytes.")
print(data)

# Test LZMADecompressor in one-shot mode

# Source data contains a short string of ASCII text
data = b"This is a test. This is only a test."

# Create a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
