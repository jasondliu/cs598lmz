import ctypes
ctypes.cast(10, ctypes.py_object)

def test_c_cast():
    assert ctypes.cast(12, ctypes.py_object) == 12
    assert ctypes.cast("hello", ctypes.py_object) == "hello"
    raises(TypeError, ctypes.cast, "hello", ctypes.c_int)

def test_byref():
    assert ctypes.byref(12) == ctypes.cast(12, ctypes.POINTER(ctypes.c_uint))
    assert ctypes.byref("hello") == ctypes.cast("hello", ctypes.POINTER(ctypes.c_char_p))

def test_sizeof():
    assert ctypes.sizeof(ctypes.c_int) == 4
    assert ctypes.sizeof(ctypes.c_int(12)) == 4
    assert ctypes.sizeof(ctypes.c_int()) == 4
    assert ctypes.sizeof(ctypes.c_int(12)) == 4
    assert ctypes.sizeof(ctypes.c_char_p
