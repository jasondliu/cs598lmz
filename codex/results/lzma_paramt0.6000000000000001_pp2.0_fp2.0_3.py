from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#
#  lz4
#
from lz4 import decompress
decompress(data)

#
#  zstd
#
from zstandard import ZstdDecompressor
ZstdDecompressor().decompress(data)

#
#  bz2
#
import bz2
bz2.decompress(data)

#
#  gzip
#
import gzip
gzip.decompress(data)

#
#  LZF
#
from lzf import decompress
decompress(data)

#
#  LZW
#
from lzw import decompress
decompress(data)

#
#  LZSS
#
from lzss import decompress
decompress(data)

#
#  LZRW3
#
from lzrw3 import decompress
decompress(data)

#
#  LZJB
#
from lzjb import decompress
decompress(data)

#
# 
