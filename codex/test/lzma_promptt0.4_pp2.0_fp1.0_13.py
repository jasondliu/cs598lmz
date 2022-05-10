import lzma
# Test LZMADecompressor

# Test decompression of empty data
d = lzma.LZMADecompressor()
d.decompress(b'')
d.decompress(b'')
d.decompress(b'')
d.decompress(b'')
d.decompress(b'')

# Test decompression of empty data with max_length
d = lzma.LZMADecompressor()
d.decompress(b'', max_length=0)
