import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

class T(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

print(S.__dict__)
print(T.__dict__)
