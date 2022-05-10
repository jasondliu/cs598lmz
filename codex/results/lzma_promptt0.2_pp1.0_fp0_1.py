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
            print('Output:', data)
            data = decompressor.unconsumed_tail
    else:
        break

# Flush the decompressor
data = decompressor.flush()
print('Flushed:', data)

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
            print('Output:', data)
            data = decompressor.unconsumed_tail
   
