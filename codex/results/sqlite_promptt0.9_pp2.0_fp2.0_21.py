import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared", uri=True) with:
# $ LD_PRELOAD=`pwd`/libsqlite3x.so python3 this.py

# https://github.com/SQLite3-Backer/sqlite3x/issues/1

_c = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
_l = threading.Lock()
assert "_c._ZN6sqlite324auth_start_interfaceEPKNS_11sqlite3_authE" in dir(_c)
assert "_c._ZN6sqlite3N5Btree16lockBtreeMutexEv" in dir(_c)


def _wrapped(*args):
    ret = None

    while ret is None:
        _l.acquire()
        try:
            ret = func(*args)
        except Exception:
            pass
        finally:
            _l.release()
    return ret


def register():
    global func
    global _l

    old_lock = _c._ZN
