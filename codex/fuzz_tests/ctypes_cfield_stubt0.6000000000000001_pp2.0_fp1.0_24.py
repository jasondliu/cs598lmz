import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField._type_ = ctypes.CField
ctypes.CField._length_ = 1

def test(lib, src):
    if not lib:
        print('SKIP')
        raise SystemExit
    ffi = cffi.FFI()
    ffi.set_source('_lib', src, libraries=[lib])
    ffi.cdef("""
        struct {
            int x;
        } s;
    """)
    ffi.compile(verbose=True)
    from _lib import ffi, lib
    assert ffi.typeof(ffi.C.s) is ctypes.CField
    assert ffi.typeof(ffi.C.s.x) is ctypes.CField
    assert ffi.sizeof(ffi.C.s) == 4
    assert ffi.offsetof(ffi.C.s, 'x') == 0
    assert ffi.alignof(ffi.C.s) == 4
    assert ffi.typeof(ffi.C.s)._type_
