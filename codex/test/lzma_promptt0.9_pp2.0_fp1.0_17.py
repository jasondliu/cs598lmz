import lzma
# Test LZMADecompressor for empty data
comp = lzma.LZMADecompressor()
data = b'\x5d\x00\x00\x80\x00\xff\xff'
result = comp.decompress(data)
print("Empty result:", repr(result))

comp = lzma.LZMADecompressor()
data = b'\x5d\x00\x00\x80\x00\xff'
result = comp.decompress(data)
print("Empty result:", repr(result))

# Update with half the inital stream
comp = lzma.LZMADecompressor()
result = comp.decompress(data[:3])
result = comp.decompress(data[3:])
print("Empty result:", repr(result))

# Try to update with more than the initial stream
