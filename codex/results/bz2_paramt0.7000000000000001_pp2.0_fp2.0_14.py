from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = func_obj(BZ2Decompressor, BZ2Decompressor.decompress)

from lzma import LZMADecompressor, lzma
LZMADecompressor.decompress = func_obj(LZMADecompressor, LZMADecompressor.decompress)
lzma.decompress = func_obj(lzma, lzma.decompress)

from brotli import BrotliDecompressor, brotli
BrotliDecompressor.decompress = func_obj(BrotliDecompressor, BrotliDecompressor.decompress)
brotli.decompress = func_obj(brotli, brotli.decompress)

from zlib import decompress, decompressobj
decompress = func_obj(decompress)
decompressobj.decompress = func_obj(decompressobj, decompressobj.decompress)

try:
    from snappy import decompress
except ImportError:
    pass


