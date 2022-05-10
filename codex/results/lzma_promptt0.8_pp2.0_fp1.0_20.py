import lzma
# Test LZMADecompressor.eof()

with open('lzma_alone.xz', 'rb') as fp:
    data = fp.read()

# data is compressed with LZMA_PRESET_EXTREME, which makes it impossible to
# know the uncompressed size. First decompress the whole file, and then verify
# that decompressing again yields an empty result.
dec = lzma.LZMADecompressor()
result1 = dec.decompress(data)
result2 = dec.decompress(b"")
assert dec.eof()
# Test LZMADecompressor on more input than needed

with open('lzma_alone.xz', 'rb') as fp:
    data = fp.read()

dec = lzma.LZMADecompressor()
result1 = dec.decompress(data)
dec.decompress(data)
assert dec.unused_data == data
# Test LZMADecompressor.flush() on LZMA_FINISH mode

dec = lzma.LZ
