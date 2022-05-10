from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# LZMA - Compress with Python LZMA library
from lzma import LZMACompressor
LZMACompressor().compress(data)

# RLE - Run-length encoding
# PPM - Packed Pixel Mode
# LZW - Lempel-Ziv-Welch
# DEFLATE - Deflate (LZ77) + Huffman
# ZLIB - DEFLATE, but with a header and a checksum
# GZIP - ZLIB, but with a header, a checksum, and a footer
# BZIP2 - Burrows-Wheeler + Huffman
# XZ - LZMA2 + LZMA
# LZ4 - Lempel-Ziv + Huffman
