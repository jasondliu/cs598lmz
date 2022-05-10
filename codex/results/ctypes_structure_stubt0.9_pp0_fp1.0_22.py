import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(S) # TypeError: __new__() got an unexpected keyword argument '_type_'
    y = ctypes.c_int

S2 = ctypes.POINTER(S)

print [type(f) for f in (S.x, S.y)]
print [type(f) for f in (S2.x, S2.y)]
</code>

