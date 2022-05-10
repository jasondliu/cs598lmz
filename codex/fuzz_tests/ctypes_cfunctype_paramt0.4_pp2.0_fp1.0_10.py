import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The callback function
def py_func(n):
    print "py_func", n
    return n

# The callback function wrapper
@FUNTYPE
def c_func(n):
    return py_func(n)

# The callback function pointer
c_func_ptr = FUNTYPE(c_func)

# The C function
def c_call_back(f, n):
    return f(n)

# Call the C function
print c_call_back(c_func_ptr, 42)
</code>

