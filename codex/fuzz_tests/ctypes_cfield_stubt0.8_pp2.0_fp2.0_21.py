import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cast():
    s = S()
    py.test.raises(TypeError, ctypes.wintypes.HWND, s.x)
    assert type(s.x) is ctypes.c_int

    hwnd = ctypes.wintypes.HWND(s.x)
    assert type(hwnd) is ctypes.wintypes.HWND
    assert not isinstance(hwnd, ctypes.CField)

def test_unwrap():
    s = S()
    hwnd = ctypes.wintypes.HWND(s.x)
    assert int(hwnd) == 0
    #
    assert int(ctypes.byref(hwnd)) == ctypes.addressof(s)
    #
    assert hwnd.value == s.x.value

#
# The rest of this file tests internal implementation details of the
# _winapi module.

def test_byref_buffer():
    import sys
    #
    b = ctypes._winapi.byref_buffer
