import lzma
# Test LZMADecompressor
x = lzma.LZMADecompressor()

# Test LZMAFile
# with open(__file__, "rb") as input:
#     with lzma.open(input, "rb") as compressed:
#         print(compressed.read())

# Test LZMAFile
with open(__file__, "rb") as input:
    with lzma.open(input, "rb") as compressed:
        print(compressed.read())

# Test compress
# data = b"Hello world!"
# compressed = lzma.compress(data)
# print(compressed)

# Test compress
data = b"Hello world!"
compressed = lzma.compress(data)
print(compressed)

# Test decompress
# compressed = b"Hello world!"
# decompressed = lzma.decompress(compressed)
# print(decompressed)

# Test decompress
compressed = b"Hello world!"
decompressed = lzma.decompress(compressed)
print(decompressed
