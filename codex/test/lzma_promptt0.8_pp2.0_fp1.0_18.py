import lzma
# Test LZMADecompressor for bugs
compressor = lzma.LZMADecompressor()
compressor.decompress(b'\x00' * 8)
compressor.decompress(b'\x00' * 8)
# Test LZMAFile for bugs
