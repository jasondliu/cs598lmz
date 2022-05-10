import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

# with open('data/enwik8', 'rb') as f:
#     decompressor = lzma.LZMADecompressor()
#     with open('data/enwik8.txt', 'wb') as g:
#         while True:
#             chunk = f.read(1024)
#             if not chunk:
#                 break
#             g.write(decompressor.decompress(chunk))
#     print(decompressor.unused_data)
#     assert decompressor.eof
#     g.write(decompressor.flush())

# # Test LZMACompressor
# # https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor

# # with open('data/enwik8.txt', 'rb') as f:
# #     compressor = lzma.LZMACompressor()
# #     with open('data/en
