import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert issubclass(type(S.x), ctypes.CField)

assert type(S.x) is not ctypes.CField

class C(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

assert ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_OptimizeFlag').value == 1

assert "don't know how to convert parameter" in ctypes.pythonapi.PyString_FromString.restype.__doc__

def foo(x):
    return x

foo._flags_ = 1

assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(foo)(2) == 2

assert not hasattr(ctypes.c_int, 'offset')
assert type(ctypes.c_int(0).offset) is int

assert ctypes.pythonapi.PyLong_AsLongLong.restype.__doc__ == "don't know how to convert return value"
assert ctypes.pythonapi.PyLong_AsLongLong.
