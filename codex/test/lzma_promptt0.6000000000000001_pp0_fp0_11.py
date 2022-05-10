import lzma
# Test LZMADecompressor
compressed = b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r$\x04\x00\x19\x85\x8cH'
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
