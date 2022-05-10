from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# This is the same as the example in the documentation:
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.decompress


# The following code creates a file with the compressed data:
with open('test.lzma', 'wb') as f:
    f.write(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# The following code decompresses the file using the lzma module:
with open('test.lzma', 'rb') as f:
    file_content = f
