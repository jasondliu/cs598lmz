import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

ctypes.CStruct = type(T)

# ____________________________________________________________

def test_create_string_buffer():
    b = ctypes.create_string_buffer(10)
    assert len(b) == 10
    assert b[0] == '\x00'

def test_create_unicode_buffer():
    b = ctypes.create_unicode_buffer(10)
    assert len(b) == 10
    assert b[0] == u'\x00'

def test_get_errno():
    assert ctypes.get_errno() == 0

def test_set_errno():
    ctypes.set_errno(42)
    assert ctypes.get_errno() == 42

def test_get_last_error():
    assert ctypes.get_last_error() == 0

def test_set_last_error():
    c
