import lzma
# Test LZMADecompressor.

# Create a LZMADecompressor object.
decompressor = lzma.LZMADecompressor()

# Feed data to the decompressor object.
# The data is read from a file-like object.
with open('lorem.txt.xz', 'rb') as input, \
     open('lorem-decompressed.txt', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Flush the decompressor by feeding it empty bytes.
output.write(decompressor.flush())

# The decompressor object can be used only once.
# After it has been flushed, it cannot be used anymore.
# To decompress another chunk of data, create a new object.

# The LZMADecompressor class also supports the context management protocol.
# This is equivalent to the above example:
with open('lorem.txt.xz', 'rb') as input, \
     open('lorem
