import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype(lib, args):
    ffi = FFI()
    ffi.cdef("int printf(const char *, ...);")
    lib = ffi.verify("#include <stdio.h>")
    c_printf = lib.printf

    ffi = FFI()
    ffi.cdef("int myfunc(int (*callback)(int, int), int, int);")
    lib = ffi.verify("""
        #include <stdio.h>
        int myfunc(int (*callback)(int, int), int a, int b)
        {
            return callback(a, b);
        }
    """)

    def callback(a, b):
        print("got: %d %d" % (a, b))
        return a + b

    funcptr = ffi.typeof("int(*)(int,int)")
    cb = funcptr(callback)

    assert lib.myfunc(cb, 100, 20) == 120
    #
    ffi = FFI()
    ffi.cdef
