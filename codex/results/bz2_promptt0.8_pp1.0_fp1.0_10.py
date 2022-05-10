import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
with open('compressed_files/reviews.bz2', 'rb') as file, open('reviews.txt', 'wb') as out_file:
    for data in iter(lambda: file.read(100 * 1024), b''):
        out_file.write(decompressor.decompress(data))

# If a file is too big, we can do this in chunks as shown above
# 
# # Test BZ2Compressor

# compressor = bz2.BZ2Compressor()
# with open('reviews.txt', 'rb') as file, open('reviews.bz2', 'wb') as out_file:
#     for data in iter(lambda: file.read(100 * 1024), b''):
#         out_file.write(compressor.compress(data))
#     out_file.write(compressor.flush())

# # Iterate through lines and write to file
# with bz2.BZ2File('reviews.bz2', 'wb
