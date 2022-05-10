import lzma
# Test LZMADecompressor on a file

with lzma.open('data.xz', 'rb') as fin:
    with open('data.txt', 'wb') as fout:
        for data in iter(lambda: fin.read(100 * 1024), b''):
            fout.write(data)

# Use LZMADecompressor to decompress a file

with lzma.open('data.xz', 'rb') as fin:
    with open('data.out', 'wb') as fout:
        decompressor = lzma.LZMADecompressor()
        for data in iter(lambda: fin.read(1024), b''):
            fout.write(decompressor.decompress(data))
        fout.write(decompressor.flush())

# Use LZMADecompressor.decompress() to decompress a file

with lzma.open('data.xz', 'rb') as fin:
    with open('data.out', 'wb') as fout:
        decompressor = lzma.LZMADec
