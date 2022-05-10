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
