import _struct

from . import _base
from . import _util
from . import _error
from . import _const

from . import _lzma_cffi

if _util.PY3:
    _long_type = int
    _int_types = (int,)
else:
    _long_type = long
    _int_types = (int, long)


class LZMACompressor(_base.BaseCompressor):
    """Compress data in LZMA format.

    The data to be compressed can be broken up in multiple chunks. Each chunk
    of data must be passed to the compressor object using the *compress()*
    method. The compressor object can be used as a context manager, in which
    case the *close()* method is called when leaving the context.

    The LZMA format supports a limited form of random access to the
    compressed data. Each chunk of compressed data is associated with a
    chunk of uncompressed data. This means that if you want to decompress
    a part of the compressed data, you must first decompress the entire
    chunk containing the desired data.
