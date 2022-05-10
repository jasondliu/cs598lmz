from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = _wrap_decompressor(
    BZ2Decompressor.decompress,
    'bz2_decompress',
    BZ2Decompressor,
    'decompress',
    )

# The lzma module has a decompress() that takes the uncompressed size
from lzma import decompress as _lzma_decompress, LZMADecompressor
def _lzma_decompress2(data, max_length=None):
    return _lzma_decompress(data, max_length=max_length)
LZMADecompressor.decompress = _wrap_decompressor(
    _lzma_decompress2,
    'lzma_decompress',
    LZMADecompressor,
    'decompress',
    )
