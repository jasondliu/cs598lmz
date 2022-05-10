import weakref

from . import _core
from . import _util
from . import _ffi

__all__ = ['Library', 'LibraryLoader', 'ffi']

class LibraryLoader(_core._LibraryLoader):
    """Loads a shared library and provides access to its symbols.
    """
