import ctypes
# Test ctypes.CFUNCTYPE()
# This function matches the prototype of the function we want
# to wrap.
def u_strlen(u):
    return len(u)

# Now we define a pointer to the above function
u_strlen_ptr = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_wchar_p)(u_strlen)

# Now we can assign it to the libucd
