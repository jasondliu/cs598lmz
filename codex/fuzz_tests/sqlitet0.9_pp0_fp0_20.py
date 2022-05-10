import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

# Step 1: Find sqlite3.dll on the filesystem
dll_path = ctypes.util.find_library('sqlite3')
print dll_path
# Step 2: Load the DLL into the process (this will raise an error
# if the DLL does not exist or if there is an error in the DLL)
dll = ctypes.CDLL(dll_path)
print dll
# Step 3: Iterate over all exported symbols in the DLL and verify
# that the symbol can be found on the DLL
for fn in ['sqlite3_open', 'sqlite3_open_v2', 'sqlite3_open16',
           'sqlite3_close',
           'sqlite3_threadsafe', 'sqlite3_enable_shared_cache',
           'sqlite3_key', 'sqlite3_rekey', 'sqlite3_rekey_v2',
           'sqlite3_overload_function', 'sqlite3_enable_load_extension',
           'sqlite3_load_extension', 'sqlite3_auto_extension
