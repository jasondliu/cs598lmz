import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor object
while True:
    if data:
        data = decompressor.decompress(data)
        print(data)
        if data:
            print(data)
            break
    if decompressor.eof:
        break
    data = input_file.read(1024)
    if not data:
        decompressor.flush()

# Flush the decompressor object
data = decompressor.flush()
print(data)

# Clean up
decompressor.close()

# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor object
while True:
    if data:
        data = decompressor.
