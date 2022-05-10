import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# Get the address of the function
addr = ctypes.cast(func, ctypes.c_void_p).value

# Convert to function pointer
ptr = FUNTYPE(addr)

# Call the function
ptr()
</code>

