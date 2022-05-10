import weakref

from . import _ffi
from . import _lib
from . import _util
from . import _winreg
from . import _winreg_ffi

__all__ = [
    'RegistryKey',
    'HKEY_CLASSES_ROOT',
    'HKEY_CURRENT_USER',
    'HKEY_LOCAL_MACHINE',
    'HKEY_USERS',
    'HKEY_PERFORMANCE_DATA',
    'HKEY_CURRENT_CONFIG',
    'HKEY_DYN_DATA',
]


class RegistryKey(object):
    """A handle to a registry key.

    This class is a context manager, so it can be used in a with statement.
    When the context manager is closed, the handle is released.
    """

    def __init__(self, handle):
        self._handle = handle
        self._closed = False

    def __repr__(self):
        return '<{0} {1:#x}>'.format(type(self).__name__, self._handle)

    def
