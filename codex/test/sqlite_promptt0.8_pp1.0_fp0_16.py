import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(None) and sqlite3.connect(0)
# and that they use the shared cache.
# Test the type of an sqlite3_stmt
# Test that SQLITE_OPEN_SHAREDCACHE is set by
# both sqlite3.connect(0) and sqlite3.connect(None)

shared_locks = threading.RLock()

def get_shared_locks():
    return shared_locks

class SqliteSharedCache(BaseSharedCache):

    def get_lib(self):
        # Locates the sqlite library
        libs = [ctypes.util.find_library('sqlite3')]

        if os.name == 'nt':
            # Windows is even more peculiar
            libs.extend(['sqlite3.dll', 'libsqlite3.dll'])

        for lib in libs:
            try:
                return ctypes.CDLL(lib)
            except:
                pass
        else:
            raise Exception('Unable to locate sqlite DLL.')

