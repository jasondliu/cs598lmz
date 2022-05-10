from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# bz2.decompress(compressed_data)

# decompressed_data = bz2.decompress(compressed_data)
# print(decompressed_data)

# with open('test.txt', 'rb') as f:
#     compressed_data = f.read()
#
# with open('test.txt.bz2', 'wb') as f:
#     f.write(compressed_data)

# import bz2
#
# original_data = b'This is the original text.'
#
# print('Original     :', len(original_data), original_data)
#
# compressed = bz2.compress(original_data)
# print('Compressed   :', len(compressed), compressed)
#
# decompressed = bz2.decompress(compressed)
# print('Decompressed :', len(decompressed), decompressed)
