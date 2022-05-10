import ctypes
# Test ctypes.CFUNCTYPE()
# const char*
# Arguments: int
# Ignore the return value
#FuncPtr = ctypes.CFUNCTYPE(None, ctypes.c_int)

#Python version:
#FFI = FuncPtr = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)
#FFI = FuncPtr = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)

FFI = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)
print("FFI is from typing as",type(FFI))              
#print("check",sys.getrefcount(FFI))  #sys.getrefcount(FFI)

ffiFunc = FFI(lambda n: bytes("A".encode("utf8")*n, "utf8"))
print("ffiFunc is",type(ffiFunc))
#print("check",sys.getrefcount(ffiFunc))  #sys.
