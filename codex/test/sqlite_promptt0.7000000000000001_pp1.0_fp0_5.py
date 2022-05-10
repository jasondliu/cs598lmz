import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
# Test .execute()
# Test .executescript()


libc_name = ctypes.util.find_library('c')
libc = ctypes.CDLL(libc_name, use_errno=True)

c_int_p = ctypes.POINTER(ctypes.c_int)

def check_null(result, func, args):
    #print 'check_null', result, func, args
    if not result:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return result

libc.fopen.errcheck = check_null
libc.fopen.restype = ctypes.c_void_p
libc.fopen.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

libc.fread.errcheck = check_null
libc.fread.restype = ctypes.c_size_t
