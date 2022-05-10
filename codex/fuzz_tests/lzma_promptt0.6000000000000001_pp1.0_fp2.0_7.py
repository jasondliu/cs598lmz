import lzma
# Test LZMADecompressor.decompress()

# Create the decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress and print it
byte = input_file.read(1)
while byte != "":
    print(decompressor.decompress(byte))
    byte = input_file.read(1)

# Finish the decompression
print(decompressor.flush())


# Test LZMADecompressor.decompress()

# Create the decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress and print it
byte = input_file.read(1)
while byte != "":
    print(decompressor.decompress(byte))
    byte = input_file.read(1)

# Finish the decompression
print(decompressor.flush())
