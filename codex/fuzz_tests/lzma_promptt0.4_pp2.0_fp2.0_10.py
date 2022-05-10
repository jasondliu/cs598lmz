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
            print(decompressor.unused_data)
            break
    if decompressor.eof:
        break
    data = input()
    if not data:
        break

# Flush the decompressor to get any remaining data
data = decompressor.flush()
print(data)

# Print any unused data that the decompressor found
print(decompressor.unused_data)

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
data = decompressor.unconsumed_tail

# Feed data to the decompressor object
while True:
    if data:
        data = decomp
