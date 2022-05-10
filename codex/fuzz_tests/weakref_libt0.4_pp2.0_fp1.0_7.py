import weakref

from . import base
from . import errors
from . import util
from . import constants
from . import _compat
from . import _compat_lzma
from . import _compat_lz4framed
from . import _compat_snappy
from . import _compat_zstd
from . import _compat_lz4


def _get_lz4_compression_level(level):
    if level == constants.LZ4_COMPRESSION_LEVEL_MIN:
        return 1
    elif level == constants.LZ4_COMPRESSION_LEVEL_MAX:
        return 9
    else:
        return level


def _get_lz4framed_compression_level(level):
    if level == constants.LZ4_COMPRESSION_LEVEL_MIN:
        return constants.LZ4_FRAMED_COMPRESSION_LEVEL_MIN
    elif level == constants.LZ4_COMPRESSION_LEVEL_MAX:
        return constants.LZ4_FRAMED_COMPRESSION_
