import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to prime the pump
data = f.read(1)

# Decompress everything else
while True:
    try:
        data += decompressor.decompress(f.read())
    except EOFError:
        break

# Close the file and decompressor
f.close()
decompressor.flush()

# Write the decompressed data to output.txt
f = open('output.txt', 'wb')
f.write(data)
f.close()
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, just to prime the pump
data = f.read(1)

# Compress everything else
while True:
    try:
        data += compressor.compress(f.read())
    except EOFError:
        break

# Close the file and compressor
f.close()
data += compressor.flush()


