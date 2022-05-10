import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

# Wrap the function
f = FUNTYPE(func)

# Call the function
print(f(1, 2))

# Create a new function type
FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Wrap the function again
f = FUNTYPE2(func)

# Call the function
print(f(1, 2))
</code>
Output:
<code>3
3
</code>

