import lzma
# Test LZMADecompressor

import lzma

data = b"Hello world! " * 1000000

compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

print(len(data), len(compressed), compressed[:10], compressed[-10:])

decompressor = lzma.LZMADecompressor()
restored = decompressor.decompress(compressed)

print(len(restored), restored[:10], restored[-10:])

assert restored == data

# Test LZMADecompressor.decompress() with multiple calls

decompressor = lzma.LZMADecompressor()
restored = b""

for i in range(0, len(compressed), 64):
    restored += decompressor.decompress(compressed[i:i+64])

