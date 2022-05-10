import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_type():
    import _ctypes
    # This test is a bit too implementation dependent,
    # it assumes that _ctypes.PyObj_FromPtr() returns a
    # PyCObject.  This is true for PyPy, but not for CPython.
    assert type(_ctypes.PyObj_FromPtr(S.x)) is ctypes.py_object

def test_from_address():
    import _ctypes
    s = S()
    s.x = 42
    assert ctypes.py_object.from_address(ctypes.addressof(s)).value == 42

def test_from_param():
    import _ctypes
    assert ctypes.py_object.from_param(None) is None
    s = S()
    s.x = 42
    assert ctypes.py_object.from_param(s).value == 42

def test_from_address_of_function():
    import _ctypes
    assert ctypes.py_object.from_address(_ctypes.PyObj_FromPtr).value == _ctypes
