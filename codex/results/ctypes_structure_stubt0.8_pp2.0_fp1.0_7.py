import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8()

x = ctypes.c_uint8()

print('local_var', x)
print('local_var', x._objects)
print('local_var', x._objects_)

s = S()
print('struct_var', s.x)
print('struct_var', s.x._objects)
print('struct_var', s.x._objects_)
print('struct', s)
print('struct', s._objects)
print('struct', s._objects_)
