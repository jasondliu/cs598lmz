import lzma
# Test LZMADecompressor()
# decompressor = lzma.LZMADecompressor()

# with open('sample.xz', 'rb') as input_file, open('sample.txt', 'wb') as output_file:
#     parser = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
#     for data in iter(lambda: input_file.read(100 * 1024), b""):
#         output_file.write(parser.decompress(data))
# ...
#     output_file.write(parser.decompress(b""))

# decompressor.decompress(b'good morning\n')
# b'Hello, World!\n'
# decompressor.decompress(b'bad morning\n')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# lzma.LZMAError: Input format not supported by decoder
# decompressor.decompress(b'')
# b''
# decompressor.decompress(b'
