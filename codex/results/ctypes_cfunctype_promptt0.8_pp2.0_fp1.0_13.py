import ctypes
# Test ctypes.CFUNCTYPE function prototype and return type
CFUNCTYPE_test = CFUNCTYPE(ctypes.c_int)
CFUNCTYPE_test.restype = ctypes.c_double
CFUNCTYPE_test.argtypes = [ctypes.c_int]
# Test ctypes.PYFUNCTYPE function prototype and return type
PYFUNCTYPE_test = PYFUNCTYPE(ctypes.c_int)
PYFUNCTYPE_test.restype = ctypes.c_double
PYFUNCTYPE_test.argtypes = [ctypes.c_int]
# Test ctypes.WINFUNCTYPE function prototype and return type
WINFUNCTYPE_test = WINFUNCTYPE(ctypes.c_int)
WINFUNCTYPE_test.restype = ctypes.c_double
WINFUNCTYPE_test.argtypes = [ctypes.c_int]
</code>
<code>print(CFUNCTYPE_test)
</code>
<code>&lt;class 'ctypes
