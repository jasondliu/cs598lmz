import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    y = ctypes.c_int

del ctypes, S
import gc

def test_no_fields():
    S = type('S', (), {})
    ok = False
    try:
        getattr(S, '_fields_')
    except AttributeError:
        ok = True
    assert ok

def test_field_class():
    S = type('S', (object,), dict(_fields_ = [('x', int),
                                              ('y', int)]))

    assert type(S.x) is ctypes.Field
    assert type(S.y) is ctypes.Field

def test_field_access():
    S = type('S', (object,), dict(_fields_ = [('x', int),
                                              ('y', int)]))

    s = S()
    assert S.x.__get__(s) == 0
    assert s.x == 0
    assert S.x.__get__(42, S) == 0
    assert S.x.__get__(s
