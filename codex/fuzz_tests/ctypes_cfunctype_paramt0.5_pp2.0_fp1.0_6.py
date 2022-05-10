import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Create a function pointer to a function that takes an int and returns an int

def function(x):
    return x**2

f = FUNTYPE(function)

print(f(2))

# Create a function pointer to a function that takes an int and returns a void

def function(x):
    print(x)

f = FUNTYPE(function, None)

f(2)

# Create a function pointer to a function that takes no arguments and returns an int

def function():
    return 42

f = FUNTYPE(function, None, ())

print(f())

# Create a function pointer to a function that takes an int, a float and a pointer to an int

def function(x, y, z):
    z[0] = x + y
    return 42

f = FUNTYPE(function, None, (ctypes.c_int, ctypes.c_float, ctypes.POINTER(ctypes.c_int)))

z = ctypes.c_int()
f
