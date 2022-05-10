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
    data = input()
    if not data:
        break
    data = data.encode('utf-8')

# Flush the decompressor object
data = decompressor.flush()
print(data)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Feed data to the compressor object
data = b"Lots of data."
more_data = b"Even more data."
compressed = compressor.compress(data)
compressed += compressor.compress(more_data)

# Get the compressed data
final_data = compressor.flush()
compressed += final_data
