import lzma
# Test LZMADecompressor
# decompressor = lzma.LZMADecompressor()
#
# with open('test.xz', 'rb') as input, open('test.txt', 'wb') as output:
#     while True:
#         chunk = input.read(1024)
#         if not chunk:
#             break
#         output.write(decompressor.decompress(chunk))

# Test LZMACompressor
compressor = lzma.LZMACompressor()

with open('test.txt', 'rb') as input, open('test.xz', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(compressor.compress(chunk))
    output.write(compressor.flush())
