from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor()

from _bz2 import BZ2File
BZ2File = BZ2File

from gzip import GzipFile
GzipFile = GzipFile

try:
    from lzma import LZMACompressor
    LZMACompressor = LZMACompressor
except:
    LZMACompressor = None

try:
    from lzma import LZMADecompressor
    LZMADecompressor = LZMADecompressor
except:
    LZMADecompressor = None

try:
    from lzma import LZMAFile
    LZMAFile = LZMAFile
except:
    LZMAFile = None

try:
    from zlib import Decompress
    DecompressEngine = Decompress
except:
    DecompressEngine = None

try:
    from zlib import Compress
    CompressEngine = Compress
except:
    CompressEngine = None

CompressEngine = CompressEngine
DecompressEngine = Decompress
