import weakref

from . import _core
from . import _util
from . import _ffi

__all__ = ['Library', 'LibraryLoader', 'ffi']

class LibraryLoader(_core._LibraryLoader):
    """Loads a shared library and provides access to its symbols.
    """
    def __init__(self, name, mode=DEFAULT_MODE, flags=0, handle=None, use_errno=True, use_last_error=True):
        """Loads a shared library.

        :param name: name or path of the library to load.
        :param mode: mode of the library to load, see :ref:`loading-modes`.
        :param flags: optional flags to control loading, see :ref:`loading-flags`.
        :param handle: optional handle to the loaded library.
        :param use_errno: if True, a global variable 'c_errno' will be created and set to
                          the current value of the C variable errno after each call.
        :param use_last_error: if True, a global variable 'get_last_error' will
