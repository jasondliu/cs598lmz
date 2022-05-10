import ctypes

class S(ctypes.Structure):
    x = ()
S.y = (S, ctypes.c_char)

print(S.__bases__)
print(S.__dict__.keys())
print(S.__dict__['x'].__bases__[0] is tuple)
print(S.__dict__['x'] is S.x)
print(ctypes.Structure.__dict__['_fields_'])
print(S.y)
