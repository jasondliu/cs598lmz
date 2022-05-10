import lzma
# Test LZMADecompressor
comp = lzma.LZMACompressor()

assert lzma.LZMADecompressor().decompress(b'') == b''
