import ctypes
# Test ctypes.CFUNCTYPE instances
test(ctypes.CFUNCTYPE(ctypes.c_int)())
test(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)())
test(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)())
# Test ctypes.PyCFuncPtr instances
test(ctypes.PyCFuncPtr(ctypes.c_int)())
test(ctypes.PyCFuncPtr(ctypes.c_int, ctypes.c_int)())
test(ctypes.PyCFuncPtr(ctypes.c_int, ctypes.c_int, ctypes.c_int)())
