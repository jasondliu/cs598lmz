from bz2 import BZ2Decompressor
BZ2Decompressor()

from gzip import GzipFile
GzipFile(fileobj=StringIO())

from lzma import LZMACompressor, LZMADecompressor
LZMACompressor()
LZMADecompressor()

from lzma import LZMAFile
LZMAFile(fileobj=StringIO())

from lzma import open
open('', 'r')

from zlib import adler32, crc32, compress, decompress, compresslevel
adler32(b'')
crc32(b'')
compress(b'')
decompress(b'')
compresslevel(1)

from zlib import compressobj, decompressobj
compressobj()
decompressobj()

from zlib import ZLIB_VERSION
ZLIB_VERSION

from zlib import MAX_WBITS, DEFLATED, DEF_MEM_LEVEL
MAX_WBITS
DEFLATED
DEF_MEM_LEVEL

from zlib import Z_BEST_COMPRESSION, Z_BEST_SPEED
