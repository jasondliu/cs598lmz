from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma.LZMACompressor().compress(buf)) == buf

# This will return true
