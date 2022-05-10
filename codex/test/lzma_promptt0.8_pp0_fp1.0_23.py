import lzma
# Test LZMADecompressor

print("lzma.LZMADecompressor()")
decompressor = lzma.LZMADecompressor()
print("decompressor")
print("data = decompressor.decompress(b'', max_length=10) == b''")
data = decompressor.decompress(b'', max_length=10)
print("data:")
print(data)
print("data == b'':")
print(data == b'')
print("data = decompressor.decompress(b'20HELLO20WORLD', max_length=10) == b'HELLO'")
