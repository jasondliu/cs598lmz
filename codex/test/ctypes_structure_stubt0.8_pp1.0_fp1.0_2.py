import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

print(hasattr(S, 'x'))   # True
print(hasattr(S, 'y'))   # True
print(hasattr(S, 'z'))   # False

#c_int, c_long and c_longlong are not subclasses of int, so the following might not work.
x = S.x
print(isinstance(x, int))   # False 
print(isinstance(x, ctypes.c_int))   # True
