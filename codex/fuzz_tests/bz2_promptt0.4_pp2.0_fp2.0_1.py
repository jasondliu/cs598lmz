import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
# with open('../data/enwik8.bz2', 'rb') as f:
#     file_content = f.read()
#     decompressed_data = decompressor.decompress(file_content)
#     print(decompressed_data[:100])
#     print(len(decompressed_data))

# Test BZ2File
# with bz2.BZ2File('../data/enwik8.bz2', 'rb') as f:
#     file_content = f.read()
#     print(file_content[:100])
#     print(len(file_content))

# Test BZ2File with context manager
# with bz2.BZ2File('../data/enwik8.bz2', 'rb') as f:
#     for line in f:
#         print(line)
#         break

# Test BZ2File with context manager and readline
# with bz2.BZ2File('../data/enwik
