import lzma
# Test LZMADecompressor

import lzma

decompressor = lzma.LZMADecompressor()

with open('lzma_compressed', 'rb') as f:
    compressed_data = f.read()

data = decompressor.decompress(compressed_data)

print(data)

print(decompressor.unused_data)

decompressor.flush()

print(decompressor.unused_data)

print(decompressor.eof)

decompressor.decompress(b'')

print(decompressor.eof)

print(decompressor.unused_data)

print(decompressor.unconsumed_tail)

print(decompressor.eof)

# Test LZMADecompressor.decompress()

import lzma

decompressor = lzma.LZMADecompressor()

with open('lzma_compressed', 'rb') as f:
    compressed_data = f.read()

data = decompressor.
