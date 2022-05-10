import lzma
# Test LZMADecompressor improperly, just to exercise the catch_break
# in LZMADecompressor.__init__
d = lzma.LZMADecompressor()
