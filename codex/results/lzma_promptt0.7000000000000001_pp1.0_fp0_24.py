import lzma
# Test LZMADecompressor

lzma_decompressor = lzma.LZMADecompressor()

source = b"XZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00"

# This should be enough to decompress the entire stream
data = lzma_decompressor.decompress(source)

print(len(data))
print(data)

# What happens if we give LZMADecompressor more data than it needs?
# It will just ignore it.
data = lzma_decompressor.decompress(source + source)
print(data)
print(len(data))

# What happens if we give LZMADecompressor less data than it needs?
# It will stop decompressing and return whatever it has decompressed
# so far.
data = lzma_decompressor.decompress(source[:2])
print(data)
print
