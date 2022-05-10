import lzma
lzma.LZMAError

from . import _lzma

_lzma.LZMAError = LZMAError

# We need to re-export the constants defined in _lzma.
for _name in dir(_lzma):
    if _name.startswith('FILTER_'):
        globals()[_name] = getattr(_lzma, _name)
del _name

__all__ = ['LZMAError', 'LZMAFile', 'LZMACompressor', 'LZMADecompressor',
           'open', 'compress', 'decompress', 'FILTER_LZMA1', 'FILTER_LZMA2',
           'FORMAT_AUTO', 'FORMAT_XZ', 'FORMAT_ALONE', 'FORMAT_RAW']

# Constants from the LZMA SDK.
CHECK_NONE = _lzma.CHECK_NONE
CHECK_CRC32 = _lzma.CHECK_CRC32
CHECK_CRC64 = _lzma.CHECK_CRC64

