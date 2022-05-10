import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')

t = threading.Thread(target=lambda: sqlite3.connect('file:memory:?cache=shared'))
t.start()
t.join()

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

def memfd_create(name, flags):
    libc.syscall.restype = ctypes.c_long
    ret = libc.syscall(319, ctypes.c_char_p(name), flags)
    if ret == -1:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return ret

name = 'test_memfd_create'
flags = 0
#memfd = memfd_create(name, flags)
#os.close(memfd)

# Test sqlite3.connect('file:/proc/self/fd/<memfd>?cache=shared')

