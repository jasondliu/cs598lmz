import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('compressed.xz', 'rb') as f:
    data = f.read()

result = decompressor.decompress(data)

print(result)

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)

print(decompressor.needs_input)

print(decompressor.eof)
print(decompressor.unused_data)

decompressor = lzma.LZMADecompressor()

with open('compressed.xz', 'rb') as f:
    data = f.read()

result = decompressor.decompress(data)

print(result)

print(decompressor.unused_data)

print(decompressor.eof)

print(decompressor.needs_input)


print(decompressor.unused_data)

print(decompressor.eof)

