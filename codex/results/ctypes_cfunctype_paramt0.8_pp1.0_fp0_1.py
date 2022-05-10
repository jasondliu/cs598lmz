import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint32, ctypes.c_int32)

lib = ctypes.CDLL("./libpycall.so")
lib.printint.argtypes = (ctypes.c_int32,)
lib.printint.restype = ctypes.c_int32

lib.printchar.argtypes = (ctypes.c_char,)
lib.printchar.restype = ctypes.c_int32

print lib.printint(1)

print lib.printchar('@')

#set global var and get global var
lib.get_global_var.argtypes = (ctypes.c_int32,)
lib.get_global_var.restype = ctypes.c_int32
print lib.get_global_var(1)
lib.set_global_var.argtypes = (ctypes.c_int32, ctypes.c_int32)
lib.set_global_var.restype = ctypes.c_int32
print lib.set_global_var(1, 88)
print lib.get_global_var
