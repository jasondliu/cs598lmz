import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(ctypes.Structure):
    pass

class B(A):
    pass

class C(ctypes.Union):
    pass

class D(C):
    pass

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_char),
                ('c', ctypes.c_double)]

def check_field(field, name, type, offset):
    assert field[0] == name
    assert field[1] == type
    assert field[2] == offset

def check_fields(fields, names, types, offsets):
    for i in range(len(fields)):
        check_field(fields[i], names[i], types[i], offsets[i])

def test_fields():
    check_fields(S._fields_, ['x'], [ctypes.c_int], [0])

    A._fields_ = [('x', ctypes.c_int)]
    check_fields(A._fields_, ['x'
