import lzma
lzma.__name__ = "lzma"

from zstandard import ZstdCompressor, ZstdDecompressor
zstandard = ZstdCompressor()
zstandard.__name__ = "zstandard"

from bz2 import BZ2Compressor, BZ2Decompressor
bz2 = BZ2Compressor()
bz2.__name__ = "bz2"

from gzip import GzipFile, GzipFile
gzip = GzipFile(mode="wb", compresslevel=6)
gzip.__name__ = "gzip"

from lz import LZ
lz = LZ(level=1)
lz.compress = lz.compress_data
lz.decompress = lz.decompress_data
lz.__name__ = "lz"

from brotli import BrotliCompressor, BrotliDecompressor
brotli = BrotliCompressor(quality=9, lgwin=22)
brotli.__name__ = "brotli"

compressors =
