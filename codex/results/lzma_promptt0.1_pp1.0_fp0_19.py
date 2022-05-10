import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor
while True:
    if data:
        data = decompressor.decompress(data)
        print(data)
        if data:
            break
    data = input()
    if not data:
        break

# Flush any remaining data
data = decompressor.flush()
print(data)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress some data
data = compressor.compress(b"Hello world!")
print(data)

# Flush the compressor to get any remaining data
data = compressor.flush()
print(data)

# Test LZMAFile

# Open a file for reading
with lzma.open("file.xz", "rb") as input:
    # Open a file for writing
    with l
