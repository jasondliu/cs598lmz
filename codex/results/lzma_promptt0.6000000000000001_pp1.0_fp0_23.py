import lzma
# Test LZMADecompressor

# Compress a string
cobj = lzma.LZMACompressor()
compressed = cobj.compress(b"This is a test")
compressed += cobj.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMADecompressor.seek()

# Compress a string
cobj = lzma.LZMACompressor()
compressed = cobj.compress(b"This is a test")
compressed += cobj.flush()

decompressor = lzma.LZMADecompressor()

# Seek to the end of the compressed data, then try to decompress.
# This should fail, because the compressed data ends before the
# stream ends.
decompressor.seek(len(compressed), 0)
try:
    decompressed = decompressor.decompress()
except lzma.LZMAError:
    print("End of compressed data")

# Seek
