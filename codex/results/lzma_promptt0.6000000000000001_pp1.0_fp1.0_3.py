import lzma
# Test LZMADecompressor

# Test with a file containing the magic number of a LZMA file
# and a valid checksum.  This should not cause any exception.
f = open("lzma_magic.dat", "rb")
decompressor = lzma.LZMADecompressor()
decompressor.decompress(f.read())

# Test with a file containing the magic number of a LZMA file
# and an invalid checksum.  This should raise an exception.
f = open("lzma_magic_invalid_checksum.dat", "rb")
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(f.read())
except lzma.LZMAError:
    pass
else:
    raise Exception("Expected exception not raised")

# Test with the empty string.  This should raise an exception.
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(b'')
except lzma.LZMAError:
    pass
