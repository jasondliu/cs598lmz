import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(b'\x5d\x00\x00\x80\x0b\xff'))
print(decompressor.decompress(b'\x7f\xff'))
print(decompressor.decompress(b'\x00'))

print(decompressor.unused_data)

decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(b'\x5d\x00\x00\x80\x0b\x00'))

print(decompressor.unused_data)
