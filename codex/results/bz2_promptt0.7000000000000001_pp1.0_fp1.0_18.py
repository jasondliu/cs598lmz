import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

file = open('decompress_bz2.txt', 'rb')
decompressed_data = decompressor.decompress(file.read())
file.close()

file = open('uncompressed_bz2.txt', 'wb')
file.write(decompressed_data)
file.close()
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

file = open('compressed_bz2.txt', 'wb')
for data in ['Hello ', 'World!', '\n', 'Welcome to files IO !']:
    compressed_data = compressor.compress(data)
    file.write(compressed_data)

compressed_data = compressor.flush()
file.write(compressed_data)
file.close()
 
# Test BZ2File

file = open('compressed_bz2.txt', 'rb')
bz2_file = bz2.BZ2File('uncompressed
