import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ,
                                 check=lzma.CHECK_NONE,
                                 preset=9)
compressor.compress(b"Hello, world!")
compressor.compress(b" Goodbye, world!")
compressor.flush()
compressed_data = compressor.compress(b" Goodbye, world!")
print(compressed_data)
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ,
                                     check=lzma.CHECK_NONE)
decompressed_data = decompressor.decompress(compressed_data)
print(decompressed_data)

# Test LZMAFile
import io
import os
import tempfile

# Create some data to compress.
data = b"Lots of data here." * 10

# Write the compressed data to a temporary file.
temp = tempfile.TemporaryFile()
with lzma.open(temp, "w") as f:

