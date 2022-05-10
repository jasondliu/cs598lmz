import lzma
lzma.decompress(data)

# lzma.decompress(data, format=lzma.FORMAT_RAW, filters=None)

print(lzma.decompress(data))
