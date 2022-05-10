import bz2
bz2_comp = bz2.BZ2Compressor()
next(bz2_comp.compress(b'hello'))

bz2_comp.flush()

bz2_comp.compress(b'hello')
bz2_comp.compress(b'hello')
bz2_comp.flush()

bz2_comp.compress(b'hello')

bz2_comp.flush(bz2.BZ_FINISH)
bz2_comp.flush(bz2.BZ_FINISH)

bz2_comp.compress(b'hello')
