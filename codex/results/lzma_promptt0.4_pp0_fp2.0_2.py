import lzma
# Test LZMADecompressor

# Decompress a file
with open('test.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('test.out', 'wb') as g:
        for buf in iter(lambda: f.read(1024 * 1024), b''):
            g.write(decompressor.decompress(buf))
        g.write(decompressor.flush())

# Decompress a stream
with open('test.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('test.out', 'wb') as g:
        while True:
            buf = f.read(1024 * 1024)
            if not buf:
                break
            g.write(decompressor.decompress(buf))
        g.write(decompressor.flush())

# Decompress a stream, one byte at a time
with open('test.lzma', 'rb') as f:
    decompressor = lzma.LZM
