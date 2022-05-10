import lzma
# Test LZMADecompressor with a stream of at most 8 bytes
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO, memlimit=8)
    
# Decompress the file.
