import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_fix_cfield_repr():
    rep = repr(S.x)
    expected = '<field \'x\' of <CField \'x\' (ctypes.c_int, -1, -1)>>\n'
    print(rep, expected)
    assert rep == expected

    rep = repr(S.x)
    expected = '<field \'x\' of <CField \'x\' (ctypes.c_int, -1, -1)>>\n'
    print(rep, expected)
    assert rep == expected

    rep = repr(S.x)
    expected = '<field \'x\' of <CField \'x\' (ctypes.c_int, -1, -1)>>\n'
    print(rep, expected)
    assert rep == expected
