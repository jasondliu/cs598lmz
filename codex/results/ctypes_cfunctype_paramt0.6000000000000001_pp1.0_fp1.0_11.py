import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x): return x*x

# convert the Python function into a C function
func = FUNTYPE(f)

# call the C function
print(func(5))

# convert the Python function into a C function
func = FUNTYPE(lambda x: x*x)

# call the C function
print(func(5))

# convert the Python function into a C function
func = FUNTYPE(lambda x: x*x*x)

# call the C function
print(func(5))

# convert the Python function into a C function
func = FUNTYPE(lambda x: x*x*x*x)

# call the C function
print(func(5))

# convert the Python function into a C function
func = FUNTYPE(lambda x: x*x*x*x*x)

# call the C function
print(func(5))

# convert the Python function into a C function
func = FUNTYPE(lambda x: x*x*x*x*x*x)

