import lzma
# Test LZMADecompressor.stream_reader
with lzma.open('sample.txt.xz') as f:
    print(f.read())

# Test LZMADecompressor.read
with lzma.open('sample.txt.xz') as f:
    c = lzma.LZMADecompressor()
    decompressed_data = c.decompress(f.read())
    print(decompressed_data)

# Test LZMAFile.read
with lzma.open('sample.txt.xz') as f:
    print(f.read())
