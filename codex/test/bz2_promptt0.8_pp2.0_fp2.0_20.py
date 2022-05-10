import bz2
# Test BZ2Decompressor
with bz2.BZ2File('example.bz2','r') as bz2_file:
    decompressor = bz2.BZ2Decompressor()
