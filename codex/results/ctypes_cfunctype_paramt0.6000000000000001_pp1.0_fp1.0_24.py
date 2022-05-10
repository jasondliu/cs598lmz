import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int, ctypes.c_int)
def cb(n):
    print("called with {0}".format(n))
    return n
cb_c = FUNTYPE(cb)

# Call the callback directly
cb_c(5)

# Convert the callback to a function pointer and then call it
cb_f = ctypes.cast(cb_c, ctypes.c_void_p)
ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
ctypes.pythonapi.PyCapsule_GetPointer.argtypes = [ctypes.py_object, ctypes.c_char_p]
ptr = ctypes.pythonapi.PyCapsule_GetPointer(cb_f, None)
addr = ctypes.cast(ptr, ctypes.c_void_p).value
print("{0}".format(addr))

# Call the callback through the function pointer
cb_c(6)
</code>


A:

This is not a bug in Python's
