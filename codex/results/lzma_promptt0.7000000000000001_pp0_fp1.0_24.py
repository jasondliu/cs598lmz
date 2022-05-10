import lzma
# Test LZMADecompressor
# Compress and decompress a string

import io
import lzma

compressor = lzma.LZMACompressor()

data = b'a'*256 + b'b'*128 + b'c'*1024 + b'd'*2048 + b'e'*128 + b'f'*256

compressed = compressor.compress(data)
compressed += compressor.flush()

print(len(data))
print(len(compressed))

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed)

print(len(decompressed))

print(decompressed == data)

del compressor, decompressor

# LZMACompressor and LZMADecompressor objects can be used as context managers.
# This ensures that the close() method is called when the compressor or
# decompressor is not needed anymore.

with lzma.LZMACompressor() as compressor:
    with lzma.LZMADecompressor() as decomp
