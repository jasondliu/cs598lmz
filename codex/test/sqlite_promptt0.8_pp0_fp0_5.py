import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

__all__ = ('errcheck', 'SQLitePyError', 'get_sqlite', 'sqlite_version',
           'sqlite_version_info', 'sqlite_version_number', 'sqlite_version_number',
           'sqlite_version_info', 'get_sqlite_lib')


class SQLitePyError(sqlite3.Error):
    '''SQLitePyError = sqlite3.Error'''
    pass


def errcheck(result, func, args):
    if result != 'ok':
        raise SQLitePyError('sqlite3.%s() failed: %s' % (func.__name__, result))
    return

errcheck = staticmethod(errcheck)


def get_sqlite_lib(platform):
    if platform.is_windows:
        if platform.is_x64:
            lib_name = 'sqlite3_x64.dll'
        elif platform.is_x86:
            lib_name = 'sqlite3.dll'
        else:
            raise NotImplementedError()

