from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# The lzma module also supports the XZ format directly:
with open('python.xz', 'rb') as input, \
     open('python.txt', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))

# The compresslevel argument can be used to adjust the compression level.
# The default value is 6, but higher and lower values can be used to tune
# the trade-offs between compression ratio and compression speed.
# Values between 1 and 9 (both inclusive) are supported.
with lzma.open('python.xz', 'w', preset=9) as output:
    output.write(b"Hello, world!")

# The format used by the xz command line tool is also supported.
with open('python.xz', 'w') as output:
    output.write(b"Hello, world!")

# ****************************************************************************
#
