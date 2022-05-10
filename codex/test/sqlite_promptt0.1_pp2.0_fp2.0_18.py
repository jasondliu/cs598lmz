import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

# https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/ffi64.c
# https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/ffi64.h
# https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/ffi.c
# https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/ffi.h
# https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/ffitarget.h
# https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/sysv.S
# https://github.com/python/cpython/bl
