import lzma
# Test LZMADecompressor
data = b'\x00\x10\x00\x00\x00"\x00\x00\x00\x00'
decomp = lzma.LZMADecompressor()
d = decomp.decompress(data)
print(d)
# The next call would raise an exception, as the entire chunk
# of compressed data should be given to decompress().
try:
    print(decomp.decompress(b'fubar'))
except lzma.LZMAError:
    print('LZMAError')
