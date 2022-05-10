import lzma
# Test LZMADecompressor with the empty bytes object.
decomp = lzma.LZMADecompressor()
decomp.decompress(b'')
# Test LZMADecompressor with invalid input data.
decomp = lzma.LZMADecompressor()
decomp.decompress(b'\x00' * 100)
# Test LZMADecompressor.decompress() with invalid input data.
decomp = lzma.LZMADecompressor()
decomp.decompress(b'\x00' * 100)
# Test LZMADecompressor with the empty bytes object.
decomp = lzma.LZMADecompressor()
decomp.decompress(b'')
# Test LZMADecompressor.decompress() with invalid input data.
decomp = lzma.LZMADecompressor()
decomp.decompress(b'\x00' * 100)
# Test LZMADecompressor.decompress() with invalid input data.
decomp = lz
