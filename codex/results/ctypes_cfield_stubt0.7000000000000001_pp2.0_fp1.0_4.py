import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_field_as_ctype():
    from cffi import FFI
    ffi = FFI()
    ffi.cdef("struct s { int x; };")
    lib = ffi.verify("""
        struct s { int x; };
    """)
    assert isinstance(lib.s.x, ctypes.CField)

def test_field_as_ctype_2():
    from cffi import FFI
    ffi = FFI()
    lib = ffi.verify("""
        struct s { int x; };
    """)
    assert isinstance(lib.s.x, ctypes.CField)

def test_field_as_ctype_3():
    from cffi import FFI
    ffi = FFI()
    import _cffi_backend
    assert isinstance(ffi._typeof_cdata_type.c_int, ctypes.CField)
    assert isinstance(_cffi_backend.types.c_int, ctypes.CField)


