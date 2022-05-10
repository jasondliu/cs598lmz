import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return None
assert isinstance(fun, FUNTYPE)


@pytest.mark.skipif(ctypes.sizeof(ctypes.c_void_p) == 4 and
                    sys.maxsize == 2147483647,
                    reason="32bit, where a pointer is generally narrower than an PyObject*")
def test_unwrap_callback():
    import _ctypes
    def f(x):
        pass

    assert _ctypes._get_callback_type(f, (ctypes.c_int,)) is FUNTYPE
    assert _ctypes._get_callback_type(f, (ctypes.c_int,), True) is FUNTYPE

    assert _ctypes._get_callback_type(f, (ctypes.c_int,), False, True) is \
           ctypes.PYFUNCTYPE(ctypes.c_int)

    assert _ctypes._get_callback_type(f, (ctypes.c_int,), True, True) is \
           ctypes.PYFUNCTYPE(ctypes.c_int)

    assert _
