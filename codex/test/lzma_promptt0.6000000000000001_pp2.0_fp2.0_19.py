import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
compressor.decompress(b'\x00')
