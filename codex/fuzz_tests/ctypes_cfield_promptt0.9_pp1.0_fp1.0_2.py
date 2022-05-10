import ctypes
# Test ctypes.CField.from_address by
# attemtpting to resolve the 'x' field of an instance of class A.
# If from_address works, the value should be an int.
# If from_address doesn't work, the value should be a float.

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_float)]
    
print(ctypes.c_int.from_address(id(A())+ctypes.sizeof(ctypes.c_void_p)))

print(ctypes.c_float.from_address(id(A())+ctypes.sizeof(ctypes.c_void_p)))

print(ctypes.c_float.from_address(id(A())+ctypes.sizeof(ctypes.c_void_p))+ctypes.c_float.from_address(id(A())+ctypes.sizeof(ctypes.c_void_p)))

print(ctypes.c_float.from_address(id(A())+ctypes.sizeof(ctypes.c_void
