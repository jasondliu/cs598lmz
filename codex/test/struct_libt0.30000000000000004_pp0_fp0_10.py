import _struct

from . import _lib
from . import _ffi
from . import _errors
from . import _types
from . import _util
from . import _cdata
from . import _compat
from . import _rawffi
from . import _buffer


def _check_size(size):
    if size < 0:
        raise ValueError("size must be non-negative")

def _check_offset(offset):
    if offset < 0:
        raise ValueError("offset must be non-negative")

def _check_count(count):
    if count < 0:
        raise ValueError("count must be non-negative")

def _check_pos(pos):
    if pos < 0:
        raise ValueError("pos must be non-negative")

def _check_mode(mode):
    if not isinstance(mode, _compat.text_type):
        raise TypeError("mode must be a string")
