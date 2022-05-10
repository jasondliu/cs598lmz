import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressor.compress(b'hello world')
compressor.flush()

# Test LZMAFile
with lzma.open('file.xz', 'wt') as f:
    f.write('hello world')

with lzma.open('file.xz', 'rt') as f:
    print(f.read())

with lzma.open('file.xz', 'rt') as f:
    print(f.read(2))
    print(f.read(2))

with lzma.open('file.xz', 'rt') as f:
