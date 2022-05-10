import bz2
# Test BZ2Decompressor
fd = bz2.BZ2File("test.bz2")
fd.read()

fd.close()

# Compress
fd = bz2.BZ2File("test.bz2", "w")
