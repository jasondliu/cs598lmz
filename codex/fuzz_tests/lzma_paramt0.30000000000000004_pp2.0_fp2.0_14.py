from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# from lzma import open
# with open('file.xz', 'rb') as f:
#     file_content = f.read()

# from lzma import compress, decompress
# data = b'The quick brown fox jumps over the lazy dog.'
# compressed = compress(data)
# decompressed = decompress(compressed)
# print(decompressed == data)

# from lzma import LZMACompressor, LZMADecompressor
# compressor = LZMACompressor()
# data = b'The quick brown fox jumps over the lazy dog.'
# compressed = compressor.compress(data)
# compressed += compressor.flush()
# decompressor = LZMADecompressor()
# decompressed = decompressor.decompress(compressed)
# print(decompressed == data)

# from lzma import LZMAFile
# with LZMAFile('file.xz', 'w') as f:
#     f.write(b'Hello World!')

# from lzma import
