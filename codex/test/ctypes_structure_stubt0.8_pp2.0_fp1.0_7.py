import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()

x = ctypes.c_uint8()

print('local_var', x)
print('local_var', x._objects)
