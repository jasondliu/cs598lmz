import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared")

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

# int clone(int (*fn)(void *), void *child_stack, int flags, void *arg, ...);
_clone = libc.clone
_clone.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p),
                   ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p)
_clone.restype = ctypes.c_int

# int pthread_atfork(void (*prepare)(void), void (*parent)(void),
#                    void (*child)(void));
_pthread_atfork = libc.pthread_atfork
_pthread_atfork.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
_pthread_atfork.restype = ctypes.c_int

CL
