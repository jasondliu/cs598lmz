import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class U(ctypes.Union):
    y = ctypes.c_int
    x = S    # invalid indirection

print S.x.name
print U.y.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: '_C DataType' object has no attribute 'name'
>>>
