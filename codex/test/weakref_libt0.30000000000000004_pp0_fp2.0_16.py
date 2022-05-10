import weakref

from ctypes import (
    c_char, c_char_p, c_int, c_uint, c_ulong, c_void_p,
    POINTER, Structure, Union,
    CFUNCTYPE,
)

from . import _ffi as ffi
from . import _lib
from . import _util
from . import _constants as constants
from . import _errors as errors
from . import _types as types
from . import _functions as functions
from . import _classes as classes
from . import _objects as objects

from . import _version as version

__all__ = [
    'ffi',
    '_lib',
    '_util',
    '_constants',
    '_errors',
    '_types',
    '_functions',
    '_classes',
    '_objects',
    'version',
]

__version__ = version.__version__

# pylint: disable=invalid-name

# pylint: disable=invalid-name

# pylint: disable=
