import bz2
# Test BZ2Decompressor

# Set up the input data
data = bz2.compress(b"The quick brown fox jumps over the lazy dog!")

# Initialize the decompressor
decompressor = BZ2Decompressor()

# Decompress the input data
output = decompressor.decompress(data)
print(output)
# Decompress the input data
decompressor.decompress(data)
print(decompressor.decompress(data))
print(decompressor.eof)

decompressor.flush()
print(decompressor.unused_data)
print(decompressor.eof)
 
# Decompress the data and write it to a file
# with bz2.open("test.bz2", "wb") as output:
#     with open("test.txt", "wb") as input:
#         decompressor = BZ2Decompressor()
#         for block in iter(lambda: input.read(100 * 1024), b""):
#             output.write(decompressor.decompress(block))
#     output
