import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'hello'

class C_callback(ctypes.Structure):
    _fields_ = [('f', ctypes.c_void_p), 
                ('a0', ctypes.c_void_p), 
                ('a1', ctypes.c_void_p)]

from ctypes import _CFuncPtr

C_fptr = ctypes.POINTER(C_callback)
fptr = ctypes.byref(C_callback(fun, 0, 0))
assert(type(fptr) == C_fptr)
</code>

