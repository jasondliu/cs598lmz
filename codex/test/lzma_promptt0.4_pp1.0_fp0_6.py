import lzma
# Test LZMADecompressor

compressed = lzma.compress(b'This is a test')
compressed

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

decompressor.unused_data

