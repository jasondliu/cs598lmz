import lzma
# Test LZMADecompressor.decompress() with a data stream that's a little
# longer than the internal buffer of the decompressor.

compressed = lzma.compress(b"Hello world!")

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
