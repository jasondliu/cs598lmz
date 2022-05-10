import lzma
lzma.LZMAError

from . import _lzma
from . import _lzma_decompress

from ._lzma import *
from ._lzma_decompress import *

__all__ = _lzma.__all__ + _lzma_decompress.__all__
