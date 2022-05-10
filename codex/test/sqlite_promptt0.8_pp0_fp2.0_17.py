import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/var/tmp/nuts.db")

myl = ctypes.cdll.LoadLibrary(None)
try:
    ctypes.cdll.LoadLibrary("libc.so.6")
except:
    pass

def open_locks(locks):
    db = sqlite3.connect("/var/tmp/nuts.db")
    for l in locks:
        fd = ctypes.c_int()
        e = myl.fcntl(l.fd, myl.F_GETFD, ctypes.byref(fd))
        if e != 0:
            raise RuntimeError("fcntl F_GETFD failed: %d", e)
        fd = fd.value
        fd |= myl.FD_CLOEXEC
        e = myl.fcntl(l.fd, myl.F_SETFD, fd)
        if e != 0:
            raise RuntimeError("fcntl F_SETFD failed: %d", e)
        l.fd = e

        if l.fd == -1: continue
