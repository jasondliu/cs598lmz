import lzma
# Test LZMADecompressor.decompress()

magic = b"\xfd7zXZ\x00" + b"\x00" * 6 + b"\xff" * 2

# Test basic operation
d = lzma.LZMADecompressor()
s = d.decompress(magic)
print(len(s))
print(s)

# Test multiple calls
d = lzma.LZMADecompressor()
s = d.decompress(magic[:2])
s += d.decompress(magic[2:10])
s += d.decompress(magic[10:])
print(len(s))
print(s)

# Test flushed data
d = lzma.LZMADecompressor()
s = d.decompress(magic + b"foo")
print(len(s))
print(s)

# Test error handling
d = lzma.LZMADecompressor()
try:
    d.decompress(b"foo")
except EOFError:
    print("EOF")
