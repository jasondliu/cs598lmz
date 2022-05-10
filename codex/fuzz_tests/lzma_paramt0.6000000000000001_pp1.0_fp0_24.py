from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# the lzma module also has support for streaming compression using
# the LZMACompressor and LZMADecompressor classes

# the bz2 module provides a comprehensive interface for the bz2
# compression library
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# the bz2 module uses the open() function and the BZ2File class for
# decompression
with bz2.open('/tmp/example.bz2', 'wt') as output:
    output.write('Contents of the example file go here.\n')

# the bz2 module also supports compression objects for streaming
# compression
compressor = bz2.BZ2Comp
