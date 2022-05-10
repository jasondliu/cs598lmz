import lzma
# Test LZMADecompressor
# decompressor = lzma.LZMADecompressor()
# with open('../data/enwik8_lzma', 'rb') as f:
#     file_content = f.read()
#     decompressed_data = decompressor.decompress(file_content)
#     print(len(decompressed_data))
#     with open('../data/enwik8_lzma_decompressed', 'wb') as f:
#         f.write(decompressed_data)
# Test LZMAFile
# with lzma.open('../data/enwik8_lzma') as f:
#     file_content = f.read()
#     print(len(file_content))
#     with open('../data/enwik8_lzma_decompressed', 'wb') as f:
#         f.write(file_content)
# Test LZMAFile with buffer
# with lzma.open('../data/enwik8_lzma') as f:
#     file_content = f.read(1024
