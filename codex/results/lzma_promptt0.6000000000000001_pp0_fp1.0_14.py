import lzma
# Test LZMADecompressor.used_data
# Test on a file with an EOF marker.
# The EOF marker is not used by the decompressor, but should be counted as used.
# The decompressor should return the correct decompressed data, and the correct
# amount of used input data.

with open('lzma_eof.xz', 'rb') as f:
    data = f.read()

cdata = lzma.compress(b'x' * 100)

# Create a file with an EOF marker.
with open('lzma_eof.xz', 'wb') as f:
    f.write(cdata)
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')

d = lzma.LZMADecompressor()

# Test that the decompressor does not return an unused_data attribute.
try:
    d.unused_data
except AttributeError:
    pass
else:
    print('LZMADecompressor has an unused
