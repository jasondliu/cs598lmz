import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_int)
 
# Python wrapper.
def py_f(x,y,z):
    print(x,y,z)
    return 0
 
# Convert to CFUNCTYPE.
cf = FUNTYPE(py_f)
 
# Save pointer to function.
f_ptr = ctypes.cast(cf, ctypes.c_void_p).value

print(f_ptr)
 
# Solve problem.
ccall(lib_fname, "Solve",
      ctypes.c_int,
      ctypes.c_double,
      ctypes.c_int,
      ctypes.c_void_p,
      (1, 2, 3, f_ptr))
