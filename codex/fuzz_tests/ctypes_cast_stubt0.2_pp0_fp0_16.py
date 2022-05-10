import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV

# ____________________________________________________________

def test_py_object_from_address():
    import ctypes
    class X(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]
    x = X()
    x.x = 42
    assert ctypes.py_object.from_address(ctypes.addressof(x)).x == 42

def test_py_object_from_address_null():
    import ctypes
    raises(ValueError, ctypes.py_object.from_address, 0)

def test_py_object_from_address_invalid():
    import ctypes
    raises(ValueError, ctypes.py_object.from_address, 1)

# ____________________________________________________________

def test_c_void_p_from_address():
    import ctypes
    class X(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]
    x = X()
    x.x =
