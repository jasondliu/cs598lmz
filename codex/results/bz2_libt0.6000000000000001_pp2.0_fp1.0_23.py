import bz2
bz2.BZ2File('compressed_file.bz2').read()

# lzma
import lzma
lzma.LZMAFile('compressed_file.lzma').read()

# xz
import lzma
lzma.LZMAFile('compressed_file.xz').read()

# zlib
import zlib
zlib.decompress(b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x1a\x8c\x04<\x00\x00\x00')

# brotli
# pip3 install brotli
import brotli
brotli.decompress(b'\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x1a\x8c\x04<\x00\x00\x00')

# snappy
# pip3 install python-snappy
from snappy import decompress

