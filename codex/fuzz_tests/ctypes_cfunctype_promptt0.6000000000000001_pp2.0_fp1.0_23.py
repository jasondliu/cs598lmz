import ctypes
# Test ctypes.CFUNCTYPE.
def foo(n):
    return n+1
c_foo = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)
print(c_foo(1))

# Test ctypes.POINTER.
c_foo_pointer = ctypes.POINTER(ctypes.c_int)(foo)
print(c_foo_pointer(1))

# Test ctypes.cast.
c_foo_cast = ctypes.cast(foo, ctypes.c_int)
print(c_foo_cast(1))

# Test ctypes.pythonapi.PyCapsule_New.
from ctypes import pythonapi
from ctypes.util import find_library
from ctypes import c_void_p, c_char_p, c_size_t
class PythonCapsule(object):
    def __init__(self, py_object, name=None, destructor=None):
        if name is None:
            name = py_object.__class__.__name__
        if destructor is None:
           
