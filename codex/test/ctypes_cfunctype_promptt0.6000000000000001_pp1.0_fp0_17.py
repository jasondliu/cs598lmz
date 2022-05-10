import ctypes
# Test ctypes.CFUNCTYPE
# https://docs.python.org/3/library/ctypes.html#function-prototypes
# https://docs.python.org/3/library/ctypes.html#callback-functions
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

# https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr
# https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE

# int (*pf)();
# pf = &f;
# (*pf)();

# typedef int (*pf)();
# pf pf1 = &f;
# pf1();

# typedef int (*pf)();
# pf pf1 = &f;
# pf pf2 = pf1;
# pf2();

# typedef int (*pf)();
# pf pf1 = &f;
# pf pf2 = p
