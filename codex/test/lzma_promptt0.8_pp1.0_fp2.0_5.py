import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
compressed = lzma.compress(b'Hello world')
decomp.decompress(compressed)

'Hello world'

