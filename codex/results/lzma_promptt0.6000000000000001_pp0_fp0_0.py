import lzma
# Test LZMADecompressor

cdata = lzma.compress(b'1234567890')

decomp = lzma.LZMADecompressor()

decomp.decompress(cdata)

decomp.decompress(b'')

decomp.flush()

decomp.decompress(b'123')
decomp.flush()

decomp.decompress(b'123')
decomp.decompress(b'')
decomp.flush()

for i in range(9):
    decomp.decompress(b'1234567890')

decomp.flush()

for i in range(9):
    decomp.decompress(b'1234567890')

decomp.decompress(b'1234567890')
decomp.flush()

decomp.decompress(b'1234567890')
decomp.decompress(b'')
decomp.flush()

del decomp
# Test LZMADecompressor.seek()

cdata = lzma.compress(b
