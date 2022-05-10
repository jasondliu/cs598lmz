import weakref

from . import _base
from . import _support
from . import _util

from . import _config
from . import _errors
from . import _events
from . import _ext
from . import _ffi
from . import _lib
from . import _util
from . import _version

from . import _debug
from . import _debug_info
from . import _debug_symbols
from . import _debug_types

from . import _dwarf


__all__ = [
    'DebugInfo',
    'DebugSymbols',
    'DebugTypes',
]


_lib.dwarf_get_debug.restype = _ffi.typeof('Dwarf_Debug *')
_lib.dwarf_get_debug.argtypes = [_ffi.typeof('Dwarf_Die *')]


class DebugInfo(_base.BaseDie):
    """
    Represents the DWARF debugging information for an ELF file.
    """

