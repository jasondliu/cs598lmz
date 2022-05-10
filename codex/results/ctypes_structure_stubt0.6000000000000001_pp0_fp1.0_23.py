import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

class T(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

print(S.__dict__)
print(T.__dict__)
print(S._fields_)
print(T._fields_)

print(ctypes.sizeof(S))
print(ctypes.sizeof(T))

s = S()
t = T()
print(s.__dict__)
print(t.__dict__)

ctypes.memset(ctypes.byref(s), 0, ctypes.sizeof(S))
ctypes.memset(ctypes.byref(t), 0, ctypes.sizeof(T))
print(s.__dict__)
print(t.__dict__)

# ctypes.memset(ctypes.byref(s), 0, ctypes.sizeof(T))
# ctypes.memset(ctypes.byref(t), 0, ctypes.
