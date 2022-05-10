import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
compressor = bz2.BZ2Compressor()

data = "nihao\nhello\nthis is a test\n"
#compressed_data = compressor.compress(data)
compressed_data = bz2.compress(data)
print compressed_data
#compressed_data = compressor.flush()
print compressed_data
#decompressed_data = decompressor.decompress(compressed_data)
#decompressed_data = bz2.decompress(compressed_data)
#print decompressed_data

#f = open('read.txt', 'w')
#f.write(decompressed_data)
#f.close()

# Test BZ2File
try:
    f1 = open('read.txt', 'wb')
    f1.write(compressed_data)
    f2 = bz2.BZ2File('read.txt')
    f1.close()
    print f2.read()
    f2.close()
