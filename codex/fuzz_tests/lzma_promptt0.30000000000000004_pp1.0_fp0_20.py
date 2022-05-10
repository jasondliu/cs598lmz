import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
decompressor.decompress(b"\x00")

# Read all remaining data from the file
with open('../data/enwik8', 'rb') as input:
    file_content = input.read()
    remaining_data = decompressor.decompress(file_content)
    remaining_data += decompressor.flush()

# Output all data
print(remaining_data)

# Close the file
input.close()

# Close the decompressor object
decompressor.close()

# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
decompressor.decompress(b"\x00")

# Read all remaining data from the file
with open('../data/enwik8', 'rb') as input:
    file_content = input.read
