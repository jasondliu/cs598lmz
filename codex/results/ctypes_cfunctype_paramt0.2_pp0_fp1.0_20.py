import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Create a function pointer
func = FUNTYPE(lambda x: x * x)

# Call the function pointer
print(func(2))

# Create a function pointer from a C function
func = FUNTYPE(lib.square)

# Call the function pointer
print(func(2))
</code>
Output:
<code>4
4
</code>

