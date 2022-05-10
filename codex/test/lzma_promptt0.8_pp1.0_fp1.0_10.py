import lzma
# Test LZMADecompressor()

decompressor = lzma.LZMADecompressor()

# decompress_func = decompressor.decompress

# while True:
#     chunk = decompress_func()
#     if chunk == b'':
#         break
#     print(chunk)

# Test LZMADecompressor.decompress(data, max_length=-1)


decompressor = lzma.LZMADecompressor()

