import lzma
# Test LZMADecompressor class

# Initialize a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Give the decompressor some input data
input = b'This is some test data'

# Loop until all input is consumed
while input:
    output = decompressor.decompress(input)
    print(output)
    input = decompressor.unused_data

# Finish compression
output = decompressor.flush()
print(output)

# Create a LZMADecompressor object that decompress data in a single step
decompressor = lzma.LZMADecompressor()
output = decompressor.decompress(b'This is some test data')
print(output)

# Create a LZMADecompressor object that decompress data in multiple steps
decompressor = lzma.LZMADecompressor()
output1 = decompressor.decompress(b'This is ')
output2 = decompressor.decompress(b'some te')
output3 = decompressor.decompress(
