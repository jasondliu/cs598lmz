import bz2
# Test BZ2Decompressor.__init__ and decompress()
for args in [(), (15000,), (16384,)]:
    compress = bz2.BZ2Compressor()
