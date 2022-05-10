import lzma
# Test LZMADecompressor object

ctext = lzma.compress(b'The quick brown fox jumps over the lazy dog.')

print(ctext)

d = lzma.LZMADecompressor()
d.decompress(ctext)

print(d.unused_data)
print(d.eof)

# Decompress a file

