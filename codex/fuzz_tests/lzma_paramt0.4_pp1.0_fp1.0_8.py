from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# with open('data.xz', 'rb') as f:
#     decompressor = LZMADecompressor()
#     with decompressor.stream(f) as decomp:
#         for chunk in iter(lambda: decomp.read(1024), b''):
#             print(chunk)

# with open('data.xz', 'rb') as f:
#     decompressor = LZMADecompressor()
#     with decompressor.stream(f) as decomp:
#         with open('data.txt', 'wb') as out:
#             while True:
#                 chunk = decomp.read(1024)
#                 if not chunk:
#                     break
#                 out.write(chunk)

# with open('data.xz', 'rb') as f:
#     decompressor = LZMADecompressor()
#     with decompressor.stream(f) as decomp:
#         with open('data.txt', 'wb') as out:
#             for chunk in iter(lambda: decomp.read(1024), b
