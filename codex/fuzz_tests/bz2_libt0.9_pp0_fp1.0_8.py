import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

import zlib
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress

import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

_compressions = 'bz2 zlib lzma'.split()
_compression_names = 'BZ2 ZLIB LZMA'.split()
_compression_mod_names = name.lower() for name in _compression_names

PY2 = sys.version_info < (3,)


def detect_compression(header):
    """Given the first bytes of a file in `header`, try to detect the compression.
    Returns a compression name, `None` if no compression was detected.
    """
    magic = lambda compress: header.startswith(compress)

    if magic(bz2.BZ2File.start):
        return 'bz2
