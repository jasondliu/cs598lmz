import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
# with open('data/total_cases.csv.bz2', 'rb') as f:
#     file_content = f.read()
#     data = decompressor.decompress(file_content)
#     print(data)
# file_content = b''
# decompressor = bz2.BZ2Decompressor()
# with open('data/total_cases.csv.bz2', 'rb') as f:
#     for block in iter(lambda: f.read(100), b''):
#         file_content += decompressor.decompress(block)
# print(file_content)
# Test BZ2File
# with bz2.BZ2File('data/total_cases.csv.bz2', 'rb') as f:
#     file_content = f.read()
#     print(file_content)
# Test readlines()
# with bz2.BZ2File('data/total_cases.csv.bz2', 'rb') as f:
