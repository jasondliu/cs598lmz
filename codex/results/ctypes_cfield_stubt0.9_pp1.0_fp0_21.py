import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)

cpy_foo = py_foo
assert isinstance(cpy_foo, ctypes.CField)

assert cpy_foo.type_ == ctypes.c_char

try:
    cpy_foo.name
except AttributeError:
    pass
else:
    print('AttributeError not raised')
