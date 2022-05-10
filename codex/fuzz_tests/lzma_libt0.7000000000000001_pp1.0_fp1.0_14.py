import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

#
# lzo compression
#
import lzo
lzo_compress = lzo.compress
lzo_decompress = lzo.decompress

#
# zlib compression
#
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress

#
# bzip2 compression
#
import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

#
# snappy compression
#
import snappy
snappy_compress = snappy.compress
snappy_decompress = snappy.decompress

#
# arith
#
import arith
arith_compress = arith.encode
arith_decompress = arith.decode


#
#
#

def test_compress(alg, input_data):
    data = alg(
