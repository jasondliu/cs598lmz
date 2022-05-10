import bz2
bz2.decompress(bz2_data)

# bz2_file = bz2.BZ2File('example.bz2')
# bz2_file.read()
# bz2_file.close()

# with bz2.BZ2File('example.bz2') as bz2_file:
#     data = bz2_file.read()

# with open('example.bz2', 'rb') as input:
#     decompressor = bz2.BZ2Decompressor()
#     with open('uncompressed.txt', 'wb') as output:
#         for block in iter(lambda: input.read(100 * 1024), b''):
#             output.write(decompressor.decompress(block))

# with open('example.bz2', 'rb') as input:
#     with bz2.open(input, 'rb') as decompressor:
#         with open('uncompressed.txt', 'wb') as output:
#             for line in decompressor:
#                 output.write
