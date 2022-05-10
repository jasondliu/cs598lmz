import lzma
# Test LZMADecompressor

cdata = lzma.compress(b'1234567890')

decomp = lzma.LZMADecompressor()

decomp.decompress(cdata)

