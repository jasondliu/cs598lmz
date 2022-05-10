from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed_data)

# 'The quick brown fox jumps over the lazy dog.'

# ..or use the context manager to decompress a file:

with open('lorem.txt.xz', 'rb') as input, \
     open('lorem_decompressed.txt', 'wb') as output:
    decompressor = LZMADecompressor()
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# The decompressor object also supports the context management protocol.
# This is useful when decompressing data in a single chunk using the
# decompress() method.

with open('lorem.txt.xz', 'rb') as input, \
     open('lorem_decompressed.txt', 'wb') as output:
    with LZMADecompressor() as decompressor:
        output.write(decompressor.decompress(input.read()))

# The LZMADecompressor class also supports the
