import lzma
# Test LZMADecompressor with a single byte input
try:
    lzma.LZMADecompressor().decompress(b'a')
except Exception as v:
    print(type(v), v)

print()

# Test LZMADecompressor with a too big single byte input
try:
    lzma.LZMADecompressor().decompress(b'abcdefghij')
except Exception as v:
    print(type(v), v)

print()

# Test LZMADecompressor with a valid input
try:
    x = lzma.LZMADecompressor()
    x.decompress(b'\x00\x04\x00\x00\x00\xff\xff\xff\xff\x00')
    x.decompress(b'\xad\xd0\x0c\x00\x01\x03\x00\x00\x00\x00\x00')
    x.decompress(b'\x00\x00\x00\x00\x
