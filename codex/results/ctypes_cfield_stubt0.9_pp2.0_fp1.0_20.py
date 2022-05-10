import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def func(x):
    return 1

x = ctypes.CField()
ctypes.CField.__get__(x, None, None)

x.__eq__(x)
x.__ne__(x)

x.__hash__ = func
x.__hash__
x.x = 1
x.x = 2

x.__get__(None, None)
x.__set__(None, None)
x.__delete__(None)


class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.py_object)]

ctypes.PyCField = type(S2.x)

func(ctypes.PyCField)

x = ctypes.PyCField()
ctypes.PyCField.__get__(x, None, None)
ctypes.PyCField.__set__(x, None, None)

x.__hash__ = func
x.__hash__
x.x = 1
x.x = 2

x.__get__(None
