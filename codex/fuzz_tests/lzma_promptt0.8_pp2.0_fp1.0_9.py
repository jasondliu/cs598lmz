import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(data))

# Create an LZMA-compressed file
with lzma.open('file.xz','w') as file:
file.write(b"Hello, World!\n")
