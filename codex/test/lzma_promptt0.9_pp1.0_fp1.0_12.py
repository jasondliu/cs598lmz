import lzma
# Test LZMADecompressor class
# The data is generated by the following Python 3 code:
#   import binascii
#   import lzma
#   d = binascii.a2b_hex('5d00008001495d888a1300')
#   lzf = lzma.LZMACompressor()
#   c = lzf.compress(d)
#   lzf.flush()
#   lzd = lzma.LZMADecompressor()
#   p = lzd.decompress(c)
