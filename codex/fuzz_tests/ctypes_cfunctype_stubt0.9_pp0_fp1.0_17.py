import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 5
assert fun() == 5
# the following is illegal, so we need macros
# funcptr = ctypes.cast(fun, ctypes.c_void_p)

from cffi import FFI
ffi = FFI()
ffi.cdef("""
    #define FUNTYPE   ...
    #define FUNCPTR   ...
    #define FUNADDR(f)   ...
    #define FUNPTR_FROM_ADDR(p)   ...
""")
funcptr = ffi.cast("void *", fun)    # illegal pointer type!
funcptr2 = ffi.cast("FUNCPTR", fun)

assert funcaddr == ffi.cast("void *", funcaddr)
assert funcptr2 == ffi.cast("FUNCPTR", funcptr2)
assert ffi.addressof(fun) == ffi.cast("long", funcptr)
