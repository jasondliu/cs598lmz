import bz2
bz2_compress = bz2.BZ2Compressor()

def prepare_bz2(data):
    return bz2_compress.compress(data)

def finalize_bz2():
    return bz2_compress.flush()

def bz2_decompress(data):
    return bz2.decompress(data)

def bz2_compress_decompress(data):
    return bz2_decompress(prepare_bz2(data)+finalize_bz2())


########## zlib ##########

def zlib_compress(data):
    return zlib.compress(data)

def zlib_decompress(data):
    return zlib.decompress(data)


########## lz4 ##########

import lz4

def lz4_compress(data):
    return lz4.dumps(data)

def lz4_decompress(data):
    return lz4.loads(data)


########## l
