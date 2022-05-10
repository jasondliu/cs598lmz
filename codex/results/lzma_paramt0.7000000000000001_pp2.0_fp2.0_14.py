from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed_data)
# b'Hello World!Hello World!Hello World!Hello World!'

# # 方式二
# with lzma.LZMAFile(filename) as f:
#     file_content = f.read()
# print(file_content)

# # 方式三
# with open('somefile.xz', 'rb') as input, open('somefile', 'wb') as output:
#     with lzma.open(input) as lzma_file:
#         for line in lzma_file:
#             output.write(line)

# # 方式四
# lzc = lzma.LZMACompressor()
# lzc.compress(data)
# lzc.flush()
# lzd = lzma.LZMADecompressor()
# lzd.decompress(compressed_data)

# # 方式五
# lzc = lzma.LZMACompressor(
