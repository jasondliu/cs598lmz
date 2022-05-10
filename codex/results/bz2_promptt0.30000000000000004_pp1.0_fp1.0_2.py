import bz2
# Test BZ2Decompressor

# decompressor = bz2.BZ2Decompressor()
# decompressed_data = decompressor.decompress(compressed_data)

# print(decompressed_data)

# decompressor = bz2.BZ2Decompressor()
# for block in iter(lambda : file_object.read(100 * 1024), b''):
#     decompressed_data = decompressor.decompress(block)
#     if decompressed_data:
#         process_data(decompressed_data)
#     else:
#         print('Not enough data to decompress')
#         break

# file_object.close()

# Test BZ2File

# file_object = bz2.BZ2File('file.bz2', 'rb')
# data = file_object.read()
# file_object.close()

# print(data)

# file_object = bz2.BZ2File('file.bz2', 'rb')
# for line in file_object:
#     print(line)
#
