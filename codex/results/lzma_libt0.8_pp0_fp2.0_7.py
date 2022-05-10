import lzma
lzma_compress(text_elapsed)
#0.6159369946374352
#0.31643888858996415

#bz2
import bz2
def bz2_compress(text):
    start_time = time.time()
    bz2.compress(bytes(text,'utf-8'))
    end_time = time.time()
    elapsed = end_time - start_time
    return elapsed
bz2_compress(text_elapsed)
#0.06805598551750237
#0.031179075140971763

#zlib
import zlib
def zlib_compress(text):
    start_time = time.time()
    zlib.compress(bytes(text,'utf-8'))
    end_time = time.time()
    elapsed = end_time - start_time
    return elapsed
zlib_compress(text_elapsed)
#0.011964917648782253
#0.006197031590424016

#
