import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    pass

instance = A()
class B(ctypes.CField):
    _type_ = ctypes.c_int
    _obj_ = instance
    _name_ = 'x'

assert isinstance(B, ctypes.CField)
assert B._type_ == ctypes.c_int
assert isinstance(B._obj_, A)
assert B._name_ == 'x'
print('success')
