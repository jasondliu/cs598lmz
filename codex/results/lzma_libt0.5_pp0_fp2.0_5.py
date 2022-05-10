import lzma
lzma.LZMADecompressor = lzma.LZMADecompressor

import os

from . import _compat
from . import _util
from . import _lzma
from . import _stream
from . import _decompressor
from . import _check
from . import _container
from . import _filter


__all__ = ["LZMADecompressor"]


class LZMADecompressor(_decompressor.LZMADecompressor):

    def __init__(self, format=None, check=-1, dict_size=None, filters=None):
        super(LZMADecompressor, self).__init__(
            format=format, check=check, dict_size=dict_size, filters=filters)

    @classmethod
    def _get_decompressor(cls, format, filters):
        if format == lzma.FORMAT_RAW:
            filter = _filter.LZMAFilter(filters)
            return _lzma.LZMADecompressor(
                format
