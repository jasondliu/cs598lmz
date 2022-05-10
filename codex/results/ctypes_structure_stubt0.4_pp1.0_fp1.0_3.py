import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    _fields_ = [("x", ctypes.c_int)]

s = S()
print(s.x)
print(s.x.value)
print(s.x.__dict__)
print(s.x.__class__)
print(s.x.__class__.__bases__)
print(s.x.__class__.__bases__[0].__dict__)
print(s.x.__class__.__bases__[0].__dict__['__getattribute__'])
print(s.x.__class__.__bases__[0].__dict__['__getattribute__'].__globals__)
print(s.x.__class__.__bases__[0].__dict__['__getattribute__'].__globals__['__builtins__'])
print(s.x.__class__.__bases__[0].__dict__['__getattribute__'].__globals__['__builtins__'].__dict__)

