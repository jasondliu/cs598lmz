import lzma
# Test LZMADecompressor().decompress()
compressed = lzma.compress(b"Test")
compressor = lzma.LZMADecompressor()
compressor.decompress(compressed)
compressor.unused_data
compressor.eof
compressor.decompress(b"")
compressor.eof
compressor.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00")
# Test LZMADecompressor().decompress() with max_length
compressor.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00", max_length=0)
compressor.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00", max_length=1)
compressor.decompress(b"\x00\x00\x00\x00\x00\x00\x00\x00", max_length=2)

