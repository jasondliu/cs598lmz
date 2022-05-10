import bz2
# Test BZ2Decompressor

compressed_data = bz2.compress(b"This is a test")
print(compressed_data)

decompressor = bz2.BZ2Decompressor()

try:
    data = decompressor.decompress(compressed_data)

except EOFError:
    print("The end of the compressed data stream has been reached")

print(data)

# BZ2File

