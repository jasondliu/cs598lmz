from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# The above code is equivalent to:
decompressor = LZMADecompressor()
decompressor.decompress(data)
decompressor.flush()

# It is possible to chain decompressors. This is often
# useful when dealing with data compressed with multiple
# algorithms.

decompressor = LZMADecompressor()
decompressor.decompress(bz2.decompress(data))
decompressor.flush()

# The decompressor object can also be used as a context
# manager. This is useful for dealing with files.

with open('compressed_file.xz', 'rb') as input, \
     open('uncompressed_file', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# For more information, please see the documentation at
# https://
