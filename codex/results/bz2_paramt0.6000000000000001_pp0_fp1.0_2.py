from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Writing compressed data to a file
with open('compressed_file.bz2', 'wb') as f:
    f.write(compressed_data)

# Reading compressed data from a file
with open('compressed_file.bz2', 'rb') as f:
    compressed_data = f.read()

# Decompressing the data
data = BZ2Decompressor().decompress(compressed_data)

# The LZMA file format
import lzma
with open('somefile.xz', 'rb') as input, open('somefile.txt', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))

# Creating a compressed file from scratch
import lzma
with open('somefile.txt', 'rb') as input, open('somefile.xz', 'wb') as output:
    compressor = lz
