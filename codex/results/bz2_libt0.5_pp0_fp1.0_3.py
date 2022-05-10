import bz2
bz2.BZ2Compressor()

# bz2.BZ2Compressor(compresslevel=9)
# bz2.BZ2Compressor(compresslevel=1)
# bz2.BZ2Compressor(compresslevel=0)

# bz2.BZ2Compressor(compresslevel=9).compress(b'kot kota')
# bz2.BZ2Compressor(compresslevel=1).compress(b'kot kota')
# bz2.BZ2Compressor(compresslevel=0).compress(b'kot kota')

# bz2.BZ2Compressor(compresslevel=9).compress(b'kot kota') + bz2.BZ2Compressor(compresslevel=9).flush()
# bz2.BZ2Compressor(compresslevel=1).compress(b'kot kota') + bz2.BZ2Compressor(compresslevel=1).flush()
# bz2.BZ2Compressor(comp
