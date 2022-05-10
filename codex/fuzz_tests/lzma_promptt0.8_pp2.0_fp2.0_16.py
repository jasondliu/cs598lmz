import lzma
# Test LZMADecompressor as a context manager
with lzma.LZMADecompressor(format=lzma.FORMAT_RAW) as dec:
    print(dec.decompress(lzma_out))

# Test LZMADecompressor as an object
dec = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
print(dec.decompress(lzma_out))

dec = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
print(dec.decompress(lzma_out))

# Test LZMADecompressor with bogus input.
dec = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
# invalid LZMA header
try:
    dec.decompress(b'7777')
except lzma.LZMAError as e:
    print(e)

# compressed data too large
try:
    dec.decompress(b'7777777777777777
