import lzma
lzma_compress_func = lzma.compress
lzma_decompress_func = lzma.decompress
lzma_compress_size_func = lzma.compress_size

import pickle
pickle_dumps_func = pickle.dumps
pickle_loads_func = pickle.loads

import marshal
marshal_dumps_func = marshal.dumps
marshal_loads_func = marshal.loads

import gzip
gzip_compress_func = gzip.compress
gzip_decompress_func = gzip.decompress
gzip_compress_size_func = gzip.compress_size

import zlib
zlib_compress_func = zlib.compress
zlib_decompress_func = zlib.decompress
zlib_compress_size_func = zlib.compress_size

import bz2
bz2_compress_func = bz2.compress
bz2_decompress_func = b
