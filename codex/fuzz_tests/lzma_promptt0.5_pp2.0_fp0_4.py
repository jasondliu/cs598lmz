import lzma
# Test LZMADecompressor
with open('../data/test.tar.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('../data/test.tar', 'wb') as g:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            data = decompressor.decompress(chunk)
            g.write(data)
        g.write(decompressor.flush())
# Test LZMACompressor
with open('../data/test.tar', 'rb') as f:
    compressor = lzma.LZMACompressor()
    with open('../data/test.tar.lzma', 'wb') as g:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            g.write(compressor.compress(chunk))
        g.write(compressor.flush())
# Test LZMAFile
with lzma.open('../data/test.tar.lzma', 'rb') as f
