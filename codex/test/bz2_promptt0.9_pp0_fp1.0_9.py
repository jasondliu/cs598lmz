import bz2
# Test BZ2Decompressor
try:
    bz2.BZ2Decompressor(b'x')
except TypeError:
    hasBZ2 = False
else:
    hasBZ2 = True
# Test LZMADecompressor
try:
    import lzma
except:
    hasLZMA = False
