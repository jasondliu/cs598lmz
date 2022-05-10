import bz2
bz2.decompress(bz2_contents)

# bz2_contents = bz2.compress(bytes('Hello World!', 'utf-8'))
# bz2.decompress(bz2_contents)

# with open('compressed_file.bz2', 'rb') as f:
#     decompressed_data = bz2.decompress(f.read())
#     print(decompressed_data)

# with open('compressed_file.bz2', 'rb') as f:
#     with bz2.BZ2File(f) as bz2_file:
#         for line in bz2_file:
#             print(line)

# with open('compressed_file.bz2', 'rb') as f:
#     with bz2.BZ2File(f) as bz2_file:
#         print(bz2_file.readline())

# with open('compressed_file.bz2', 'rb') as f_in, open('un
