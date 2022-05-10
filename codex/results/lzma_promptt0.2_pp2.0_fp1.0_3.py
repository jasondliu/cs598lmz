import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to prime the pump
data = decompressor.unconsumed_tail

# Feed data to the decompressor until it needs more
while data:
    data = decompressor.decompress(data)
    print(data)
    data = decompressor.unconsumed_tail

# Finish the decompression
data = decompressor.flush()
print(data)

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to prime the pump
data = decompressor.unconsumed_tail

# Feed data to the decompressor until it needs more
while data:
    data = decompressor.decompress(data)
    print(data)
    data = decompressor.unconsumed_tail

# Finish the decompression
data = decompressor.flush()
print(data)

# Create a decompressor object
decompressor = lzma.LZMADecompressor
