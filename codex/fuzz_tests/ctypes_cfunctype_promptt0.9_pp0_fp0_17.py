import ctypes
# Test ctypes.CFUNCTYPE()
if 1:
    from cffi import FFI
    ffi = FFI()
    ffi.cdef("void foo(int *v);")
    lib = ffi.dlopen("./x.so")
    p = ffi.new("int *", 3)
    lib.foo(p)
    print p[0]
