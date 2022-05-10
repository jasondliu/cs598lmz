import lzma
# Test LZMADecompressor

# Decompress a file
with open('test.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('test.out', 'wb') as g:
        for buf in iter(lambda: f.read(1024 * 1024), b''):
            g.write(decompressor.decompress(buf))
