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
d.decompress(b'', max_length=0)
d.decompress(b'', max_length=0)
d.decompress(b'', max_length=0)
d.decompress(b'', max_length=0)

# Test decompression of empty data with max_length
d = lzma.LZMADecompressor()
d.decompress(b'', max_length=1)
d.decompress(b'', max_length=2)
d.decompress(b'', max_length=
