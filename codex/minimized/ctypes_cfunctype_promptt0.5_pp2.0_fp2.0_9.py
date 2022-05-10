import ctypes
int_func = ctypes.CFUNCTYPE(ctypes.c_int)
prototype = ctypes.CFUNCTYPE(int_func)
result = prototype()
result2 = result()
