import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_load_cfield():
    import _ctypes
    if ctypes.sizeof(S) == ctypes.sizeof(S.x):
        return

    py_string = ctypes.c_char.from_address(id(S))
    # 'x' is the second character of the __slots__ attribute
    cfield = _ctypes.PyObj_AsPtr(py_string)
    assert cfield.in_dll(ctypes, 'x') == S.x

def test_at_address():
    S_p = ctypes.POINTER(S)
    # The actual memory address of S.x doesn't matter,
    # as long as it is different from S_p.from_address(id(S.x)).
    addr = id(S) + ctypes.sizeof(ctypes.c_int)
    S_p.from_address(addr).contents.x = 1
    assert S.x == 1

def test_byref():
    S_p = ctypes.POINTER(S)
    p = S
