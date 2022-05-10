import lzma
# Test LZMADecompressor
# with open('test.xz', 'rb') as fp:
#     d = lzma.LZMADecompressor()
#     with open('test.txt', 'wb') as output:
#         for chunk in iter(lambda: fp.read(1024 * 1024), b''):
#             output.write(d.decompress(chunk))
#         d.decompress(b"")
#         d.flush()
#         print(d.unused_data)
#         print(d.eof)
#         print(d.needs_input)
#         print(d.needs_input())
#         print(d.buffer)
#         print(d.buffer_size)

# Test LZMADecompressor.decompress
# with open('test.xz', 'rb') as fp:
#     d = lzma.LZMADecompressor()
#     with open('test.txt', 'wb') as output:
#         output.write(d.decompress(fp.read()))
#
