import lzma
# Test LZMADecompressor.
dec = lzma.LZMADecompressor()
dec.decompress(read_bytes('pylzma-tests/testdata/lzma_alone2.xz'))
dec.decompress(read_bytes('pylzma-tests/testdata/lzma_alone2.xz'), max_length=22)
dec = lzma.LZMADecompressor(dict_size=2**30)
dec.decompress(read_bytes('pylzma-tests/testdata/lzma_alone2.xz'))
dec = lzma.LZMADecompressor(format=1)
dec.decompress(read_bytes('pylzma-tests/testdata/lzma_alone2.xz'))
dec = lzma.LZMADecompressor(lc=42, lp=10, pb=2)
dec.decompress(read_bytes('pylzma-tests/testdata/lzma_alone2.xz'))
dec = l
