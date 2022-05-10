import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(descr, *args):
    print descr
    print '  ', ctypes.CField(*args)

test("CField('x', c_int)", 'x', ctypes.c_int)
test("CField('x', c_int, 1)", 'x', ctypes.c_int, 1)
test("CField('x', c_int, 1, 2)", 'x', ctypes.c_int, 1, 2)
test("CField('x', c_int, 1, 2, 3)", 'x', ctypes.c_int, 1, 2, 3)
test("CField('x', c_int, 1, 2, 3, 4)", 'x', ctypes.c_int, 1, 2, 3, 4)
