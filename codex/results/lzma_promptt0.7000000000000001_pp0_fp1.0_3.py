import lzma
# Test LZMADecompressor class

compressed_data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

inp = BytesIO(compressed_data)
decompressor = lzma.LZMADecompressor()

# Read some compressed data
inp.read(10)

# Feed data to the decompressor object
data = decompressor.decompress(inp.read(20))

print(data)

# Read more compressed data
data = inp.read()

# Feed more data to the decompressor object
data = decompressor.decompress(data)

print(data)

# LZMAFile class

# The LZMAFile class simulates most of the methods of a file object, with the exception of the truncate() method.
# For example, it is possible to use LZMAFile in the with statement.

#
