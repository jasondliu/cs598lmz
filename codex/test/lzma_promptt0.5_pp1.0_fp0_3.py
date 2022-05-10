import lzma
# Test LZMADecompressor

print("Testing LZMADecompressor")

d = lzma.LZMADecompressor()
print(d.eof)

