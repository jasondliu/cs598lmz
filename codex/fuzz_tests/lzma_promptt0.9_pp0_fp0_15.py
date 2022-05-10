import lzma
# Test LZMADecompressor class to compress and decompress files with short strings

with open('test.txt', 'rb') as in_file, \
        lzma.open('test.xz', 'wb') as out_file:
    decompressor = lzma.LZMADecompressor()
    for line in in_file:
        out_file.write(decompressor.decompress())
    out_file.write(decompressor.flush())
# var = decompressor.decompress(n) Read at least n bytes from the set LZMA string data, 
# raise EOFError if the input stream is exhausted before n bytes can be read. 
# If the data has been exhausted and an attempt is made to decompress further data a ValueError is raised.
# The return value is the uncompressed data buffer. If the size of the uncompressed data is known 
# in advance and it is less than n, passing n does not improve performance.
print(len(decompressor.decompress()))
print(len(decompressor.decompress(len(decompressor.decompress(), )
