import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.PField = type(S.x)

def P(typ):
    if isinstance(typ, str):
        return ctypes.CField(typ)
    return S._fields_[0][1] if isinstance(typ, S) else ctypes.PField(typ)
"""

def test_printing():
    ffi = FFI()
    ffi.cdef("typedef struct { ...; } S;")
    ffi.set_source("_lib", "")
    lib = ffi.compile()
    assert repr(lib) == "<CDLL 'lib_lib.PYPA_NAME.so'>"
    #
    ffi = FFI()
    ffi.cdef("typedef struct { ...; } S;")
    ffi.set_source("_lib", "")
    ffi.compile()
    assert repr(ffi) == """<FFI for _lib.PYPA_NAME._lib (ver=%d) at ...>""" % (
        ffi._backend.version, )
