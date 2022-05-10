from lzma import LZMADecompressor
LZMADecompressor().decompress(s.encode('utf-8'))

# PART 2
import bz2
bz2.decompress(s.encode('utf-8'))

# PART 3
import gzip
gzip.decompress(s.encode('utf-8'))

# PART 4
import zlib
zlib.decompress(s.encode('utf-8'))

# PART 5
import lzma
lzma.decompress(s.encode('utf-8'))

# PART 6
import brotli
brotli.decompress(s.encode('utf-8'))

# PART 7
import zstandard
zstandard.ZstdDecompressor().decompress(s.encode('utf-8'))
