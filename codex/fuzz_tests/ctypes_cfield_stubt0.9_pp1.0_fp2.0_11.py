import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('s', S), ('t', S)]

def func(obj):
    obj.s.x = 42

def f(x):
    obj = C.from_address(x)
    func(obj)
    return obj.s.x

print(f(id(S()) + ctypes.sizeof(S)))
