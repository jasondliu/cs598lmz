import lzma
# Test LZMADecompressor

# Test that the decompressor can decompress a file compressed with the
# command-line xz tool.

with open('testdata/lzma/xz-5.0.3-x86_64-linux-gnu.tar.xz', 'rb') as f:
    cdata = f.read()

d = lzma.LZMADecompressor()
data = d.decompress(cdata)

with open('testdata/lzma/xz-5.0.3-x86_64-linux-gnu.tar', 'rb') as f:
    assert data == f.read()

# Test that the decompressor can decompress a file compressed with the
# command-line lzma tool.

with open('testdata/lzma/lzma-4.32.7-x86_64-linux-gnu.tar.lzma', 'rb') as f:
    cdata = f.read()

d = lzma.LZMADecompressor()
data = d.decompress(cdata)
