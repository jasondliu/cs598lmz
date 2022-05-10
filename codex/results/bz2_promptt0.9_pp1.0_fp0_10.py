import bz2
# Test BZ2Decompressor.__enter__() and __exit__()
with bz2.BZ2Decompressor() as dec:
    pass
 
with bz2.BZ2Compressor() as comp:
    pass
