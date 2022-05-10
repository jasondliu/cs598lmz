import lzma
# Test LZMADecompressor

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

compressed = compressor.compress(b'Hello world!')
compressed += compressor.flush()

print(compressed)

# Test LZMAFile

with lzma.open('file.xz', 'wt') as f:
    f.write('Hello world!')

with lzma.open('file.xz', 'rt') as f:
    print(f.read())

# Test LZMAError

try:
    decompressor.decompress(b'
