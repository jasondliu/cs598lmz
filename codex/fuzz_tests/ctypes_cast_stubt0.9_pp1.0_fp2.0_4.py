import ctypes
ctypes.cast(print_z(4,4), ctypes.py_object).value

print_z_float = lib.print_z
print_z_float.argtypes = [ctypes.POINTER(ctypes.c_double)]
print print_z_float(ctypes.pointer(ctypes.c_double(4))).contents

print_z_double = lib.print_z
print_z_double.argtypes = [ctypes.POINTER(ctypes.c_double)]
print print_z_double(ctypes.pointer(ctypes.c_double(-4))).contents

# if we try to use an argument of the wrong type, it will fail
#print print_z_double(ctypes.pointer(ctypes.c_int(-4))).contents

lib.add.argtypes = [ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_double),
        ctypes.POINTER(ctypes.c_double)]
lib.add.restype = ctypes.c_double

a = ctypes
