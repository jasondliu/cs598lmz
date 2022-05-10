import bz2
# Test BZ2Decompressor with EOFError exceptions.

data = open("/etc/services", "rb").read()
d = bz2.BZ2Decompressor()
