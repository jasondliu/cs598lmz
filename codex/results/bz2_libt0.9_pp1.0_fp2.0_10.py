import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress
bz2_BZ2Compressor = bz2.BZ2Compressor
bz2_BZ2Decompressor = bz2.BZ2Decompressor

try:
    from bz2 import BZ2Compressor, BZ2Decompressor
    has_bz2 = True
except ImportError:
    BZ2Compressor = BZ2Decompressor = None
    has_bz2 = False

try:
    from .lzma import LZMADecompressor, LZMACompressor
    has_lzma = True
except ImportError:
    LZMACompressor = LZMADecompressor = None
    has_lzma = False


if has_gzip:
    GzipFile = gzip.GzipFile
else:
    GzipFile = None
if has_bz2:
    BZ2File = bz2.BZ2File
else:
    BZ
