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

if __name__ == "__main__":
    dllpath = ctypes.util.find_library("sqlite3")
    dll = ctypes.CDLL(dllpath)
    c_cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(my_cb)
    dll.sqlite3_initialize()
    sm = dll.sqlite3_syscall_malloc
    sm.restype = ctypes.c_void_p
    dll.sqlite3_config(dll.SQLITE_CONFIG_SINGLETHREAD)
    dll.sqlite3_vfs_register(dll.sqlite3_vfs_find("unix-none"), 0)
    pc = sm(ctypes.c_int(len(DB_URI)))
    pc_buff = (ctypes.c_char * (len(DB_URI))).from_buffer(pc)
    ctypes.memmove(pc_buff, DB_URI, len(DB_URI))
    pvfs =
