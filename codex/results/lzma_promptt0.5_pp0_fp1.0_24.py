import lzma
# Test LZMADecompressor
with open('testdata/xz.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
    data = d.decompress(f.read())
    data == b'This is a test.\n'

with open('testdata/xz.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
    data = f.read(2)
    data = d.decompress(data)
    data = d.decompress(f.read())
    data == b'This is a test.\n'

with open('testdata/xz.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
    data = f.read(2)
    data = d.decompress(data, max_length=5)
    data == b'This '
    data = d.decompress(f.read(), max_length=5)
    data == b'is a '
    data = d.
