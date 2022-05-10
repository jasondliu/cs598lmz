import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_repr():
    # Check that the repr of a CField is the same as the repr of the
    # corresponding ctypes type.
    assert repr(S.x) == repr(ctypes.c_int)

def test_cfield_name():
    # Check that the name of a CField is the same as the name of the
    # corresponding ctypes type.
    assert S.x.__name__ == 'c_int'

def test_cfield_type():
    # Check that the type of a CField is the same as the type of the
    # corresponding ctypes type.
    assert type(S.x) == type(ctypes.c_int)

def test_cfield_doc():
    # Check that the doc of a CField is the same as the doc of the
    # corresponding ctypes type.
    assert S.x.__doc__ == ctypes.c_int.__doc__

def test_cfield_set_doc():
    # Check that the doc of a CField can be set.
    S.
