from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# decompress data
# decompressor = LZMADecompressor()
# decompressor.decompress(data)

# decompress data incrementally
# decompressor = LZMADecompressor()
# while True:
#     chunk = file.read(1024)
#     if not chunk:
#         break
#     data += decompressor.decompress(chunk)
# data += decompressor.flush()

# decompress data incrementally with multiple threads
# decompressor = LZMADecompressor()
# while True:
#     chunk = file.read(1024)
#     if not chunk:
#         break
#     data += decompressor.decompress(chunk, max_length=1024)
# data += decompressor.flush()

# decompress data incrementally with multiple threads
# decompressor = LZMADecompressor()
# while True:
#     chunk = file.read(1024)
#     if not chunk:
#         break
#     data += decompressor.decompress(chunk,
