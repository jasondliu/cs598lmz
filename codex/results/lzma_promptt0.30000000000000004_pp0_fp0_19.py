import lzma
# Test LZMADecompressor

# Test decompression of a file with a single LZMA stream

# This file was created from test/data/empty by running:
#   lzma e test/data/empty test/data/empty.xz

with open('test/data/empty.xz', 'rb') as f:
    compressed = f.read()

decompressor = lzma.LZMADecompressor()

# Decompress the whole file at once
data = decompressor.decompress(compressed)
assert data == b''

# Decompress the file in chunks
data = b''
decompressor = lzma.LZMADecompressor()
for chunk in [compressed[:10], compressed[10:]]:
    data += decompressor.decompress(chunk)
assert data == b''

# Decompress the file in chunks, with a buffer size that is not a multiple of
# the LZMA chunk size
decompressor = lzma.LZMADecompressor()
data = b''
for chunk in [compressed[:
