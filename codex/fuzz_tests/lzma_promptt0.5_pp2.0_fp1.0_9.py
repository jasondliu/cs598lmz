import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = compressor.compress(b'Hello world!')
data += compressor.flush()

decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(data))

# Test LZMADecompressor.decompress()
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'Hello world!')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/lzma.py", line 704, in decompress
#     self._buffer += self._decompressor.decompress(data, max_length)
# lzma.LZMAError: Input format not supported by decoder

# Test LZMADecompressor.flush()
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'Hello world!')
dec
