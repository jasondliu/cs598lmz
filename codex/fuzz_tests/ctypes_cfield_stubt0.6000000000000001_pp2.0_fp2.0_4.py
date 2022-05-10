import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CField_p = ctypes.POINTER(ctypes.CField)

def check_exact(S, fields):
    for field, expected in zip(S._fields_, fields):
        assert field[0] == expected[0]
        assert field[1] == expected[1]

def test_fields():
    check_exact(ctypes.c_int,
                [('value', ctypes.c_int)])
    check_exact(ctypes.c_int.in_dll(ctypes.CDLL(None), "x"),
                [('value', ctypes.c_int)])
    check_exact(ctypes.c_int * 5,
                [('0', ctypes.c_int),
                 ('1', ctypes.c_int),
                 ('2', ctypes.c_int),
                 ('3', ctypes.c_int),
                 ('4', ctypes.c_int)])
    check_exact(ctypes.c_int * 5,
                [('0', ctypes.c
