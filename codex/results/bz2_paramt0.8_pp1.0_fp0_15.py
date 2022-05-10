from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = wraps(BZ2Decompressor.decompress)(decompress)

from gzip import GzipFile
GzipFile.read = wraps(GzipFile.read)(read)

from gzip import _read_gzip_header
_read_gzip_header = wraps(_read_gzip_header)(_read_gzip_header)

from gzip import _write_gzip_header
_write_gzip_header = wraps(_write_gzip_header)(_write_gzip_header)

from gzip import compress
from gzip import decompress
from gzip import open
from gzip import write32u
from gzip import read32
from gzip import read32u
