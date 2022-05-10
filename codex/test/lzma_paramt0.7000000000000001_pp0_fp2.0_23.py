from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor
from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor


try:
    from bz2 import BZ2Decompressor
except ImportError as e:
    BZ2Decompressor = None

try:
    from lzma import LZMADecompressor
except ImportError as e:
    LZMADecompressor = None

try:
    from gzip import GzipFile, GzipDecompress
except ImportError as e:
    GzipFile = None
    GzipDecompress = None

try:
    from brotli import BrotliDecompressor
except ImportError as e:
    BrotliDecompressor = None

import zlib
ZlibDecompress = zlib.decompressobj

try:
    from snappy import SnappyDecompressor
except ImportError as e:
    SnappyDecompressor = None

