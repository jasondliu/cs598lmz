import lzma
# Test LZMADecompressor

# The LZMADecompressor class can be used to decompress data incrementally.
# It supports all the same compression options as the LZMACompressor class.

# The decompressor object can be used as a context manager.
# This ensures that the close() method is called on the decompressor object.

with lzma.LZMADecompressor() as decompressor:
    with open('lorem.xz', 'rb') as input, open('lorem.txt', 'wb') as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            output.write(decompressor.decompress(chunk))

# The decompressor object can also be used as a one-shot filter.

with open('lorem.xz', 'rb') as input, open('lorem.txt', 'wb') as output:
    output.write(lzma.decompress(input.read()))

# The decompressor object can also be used to decompress data incrementally.

decompressor = lzma
