import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
# ctypes.CDLL("./libmylib.so").my_func(FUNTYPE(myfunc))

import ctypes
lib = ctypes.CDLL("./libmylib.so")
lib.my_func.argtypes = (FUNTYPE,)
lib.my_func.restype = ctypes.c_double

lib.my_func(FUNTYPE(myfunc))
</code>

