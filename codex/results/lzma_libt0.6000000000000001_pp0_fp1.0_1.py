import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import zlib
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress

import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

import brotli
brotli_decompress = brotli.decompress
def brotli_compress(data, quality=11):
    return brotli.compress(data, quality=quality)

def do_test(compress_func, decompress_func, data_size, test_size=100000):
    data = os.urandom(data_size)
    compressed = compress_func(data)
    data_size = len(data)
    compressed_size = len(compressed)
    for i in range(test_size):
        assert decompress_func(compressed) == data
    return data_size, compressed_size


