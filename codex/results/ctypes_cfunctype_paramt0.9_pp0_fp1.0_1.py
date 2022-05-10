import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

fun_c = FUNTYPE(fun_c_py)
# fun_c.argtypes = (ctypes.c_int, ctypes.c_int)
fun_c.restype = ctypes.c_int
print(fun_c(10, 20))

# Example from:
# http://jfine-python-classes.readthedocs.io/en/latest/workbook.html
# Compile from C code:
# clang -shared -undefined dynamic_lookup -o fun.so -fPIC fun_c.c
# import fun
