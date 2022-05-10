import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x+1

# Convert a Python function to a C function pointer
C_FUNC = FUNTYPE(func)

# Pass the C function pointer to the C library
print(mylib.call_c_func(C_FUNC, 2))
</code>
This works for me. 

