import lzma
# Test LZMADecompressor
compressed = b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r$\x04\x00\x19\x85\x8cH'
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decompressed = decompressor.decompress(compressed)
decompressed

# Test LZMADecompressor.decompress() with no data
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decompressor.decompress(b'')
decompressor.decompress(b'')

# Test LZMADecompressor.decompress() with multiple calls
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decompressed = decompressor.decompress(compressed[:10])
decompressed += decompressor.decomp
