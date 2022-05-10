from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzma'

from . import _lzma

# The LZMA_CONCATENATED constant is not available in the lzma module
# in Python < 3.3.
try:
    from lzma import LZMA_CONCATENATED
except ImportError:
    LZMA_CONCATENATED = 3

from . import _compression

from ._compression import ZLIB_RUN, ZLIB_VERSION, ZLIB_STREAM_END, ZLIB_BUF_ERROR
from ._compression import ZLIB_DATA_ERROR, ZLIB_MEM_ERROR, ZLIB_NEED_DICT, ZLIB_ERRNO
from ._compression import ZLIB_STREAM_ERROR, ZLIB_DEFLATED, ZLIB_OK, ZLIB_VERNUM
from ._compression import ZLIB_NO_FLUSH, ZLIB_PARTIAL_FLUSH, ZLIB_SYNC_FLUSH
from ._compression import ZLIB_FULL_FLUSH, ZLIB_BLOCK, ZLIB_TREES
from
