import lzma
# Test LZMADecompressor

# The LZMADecompressor class supports incremental decompression.
# The decompress() method can be called multiple times with new data and the
# uncompressed data will be returned.

# The decompressor object can be used as a context manager and in that case
# the decompress() method will not need to be called in order to finish the
# decompression process.

# The example below shows how to decompress data from a file.

import lzma

with lzma.open('example.xz') as f:
    file_content = f.read()

# The example below shows how to decompress data from a file-like object.

import lzma

with open('example.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    file_content = decompressor.decompress(f.read())

# The example below shows how to decompress data incrementally.

import lzma

with open('example.xz', 'rb') as f:
    decompressor = lzma.L
