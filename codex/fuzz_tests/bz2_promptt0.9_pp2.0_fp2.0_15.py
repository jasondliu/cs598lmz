import bz2
# Test BZ2Decompressor and BZ2Compressor.

from bz2 import BZ2Compressor, BZ2Decompressor

# Use constants from bz2 module.
COMPRESSION_LEVEL = bz2.COMPRESSION_LEVEL
COMPRESSION_BUFFER_SIZE = bz2.COMPRESSION_BUVEL

compressor = BZ2Compressor()
for data in (b"", b"1", b"12", b"123", b"1234567890" * 1000):
    compressed = compressor.compress(data)
    print(len(compressed), end=' ')
compressed += compressor.flush()
print(len(compressed))

decompressor = BZ2Decompressor()
decompressed = decompressor.decompress(compressed)
if decompressed != b"1234567890" * 1000:
    raise Exception("incorrectly decompressed")
print(len(decompressed))

# Test to show that BZ2Compressor can be used with a context
# manager and that it does not compress the empty string.
with BZ2Comp
