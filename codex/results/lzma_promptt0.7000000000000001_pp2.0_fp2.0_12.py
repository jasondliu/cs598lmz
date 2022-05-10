import lzma
# Test LZMADecompressor

# Uncompressed data
data = b"Hello world! " * 100000
data += b"The end"

# Compress the data
compressed = lzma.compress(data)

# Create the decompressor
decompressor = lzma.LZMADecompressor()

# Decompress streams
stream_decompressor = lzma.LZMADecompressor()
stream = stream_decompressor.decompress(compressed)

# Decompress the raw data
decompressed = decompressor.decompress(compressed)

# Print data
print("Original:", len(data))
print("Compressed:", len(compressed))
print("Decompressed:", len(decompressed))

# Check the result
print("Check:", data == decompressed)
print("Check:", data == stream)

# Test LZMAFile

# Create the LZMAFile
with lzma.open("example.xz", "w") as output:
    output.write(data)

# Read the compressed data
