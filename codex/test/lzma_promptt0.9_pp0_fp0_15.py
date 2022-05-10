import lzma
# Test LZMADecompressor class to compress and decompress files with short strings

with open('test.txt', 'rb') as in_file, \
        lzma.open('test.xz', 'wb') as out_file:
    decompressor = lzma.LZMADecompressor()
