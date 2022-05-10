import weakref

from . import _ffi
from . import _lib
from . import _util
from . import _winreg
from . import _winreg_unicode
from . import _winreg_utf8

__all__ = [
    'HKEYType',
    'HKEY',
    'KEY_ALL_ACCESS',
    'KEY_CREATE_LINK',
    'KEY_CREATE_SUB_KEY',
    'KEY_ENUMERATE_SUB_KEYS',
    'KEY_EXECUTE',
    'KEY_NOTIFY',
    'KEY_QUERY_VALUE',
    'KEY_READ',
    'KEY_SET_VALUE',
    'KEY_WOW64_32KEY',
    'KEY_WOW64_64KEY',
    'KEY_WRITE',
    'REG_BINARY',
    'REG_DWORD',
    'REG_DWORD_BIG_ENDIAN',
    'REG_DWORD_LITTLE_ENDIAN',
    'REG_EXPAND_SZ',
    'REG_
