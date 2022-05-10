import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def function_caller(func):
    return FUNTYPE(func)

# CFFI
import cffi
ffi = cffi.FFI()
ffi.cdef("void f();")
lib = ffi.dlopen("./libcffi.so")

# Numba
from numba import jit

# Cython
import pyximport
pyximport.install(pyimport=True)
import cython

# PyPy
import pypyjit


# Function definitions

def python(func):
    def wrapper():
        func()
    return wrapper

@jit
def numba(func):
    def wrapper():
        func()
    return wrapper

@cython.locals(func="void(void)")
def cython_(func):
    def wrapper():
        func()
    return wrapper

@pypyjit.cpython_compile
def pypy(func):
    def wrapper():
        func()
    return wrapper


# Utility functions

def test_at_most
