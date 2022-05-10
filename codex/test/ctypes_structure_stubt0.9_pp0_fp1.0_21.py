import ctypes

class S(ctypes.Structure):
    x = ()
S.y = (S, ctypes.c_char)

print(S.__bases__)
print(S.__dict__.keys())
