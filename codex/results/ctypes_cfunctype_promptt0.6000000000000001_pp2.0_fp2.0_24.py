import ctypes
# Test ctypes.CFUNCTYPE.
def callback(arg):
    print("In Python: callback(" + str(arg) + ")")
    return arg
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
print("Python ctypes.CFUNCTYPE: " + str(CALLBACKFUNC))
CALLBACKFUNC.restype = ctypes.c_int
CALLBACKFUNC.argtypes = [ctypes.c_int]
print("Python ctypes.CFUNCTYPE: " + str(CALLBACKFUNC))

# Create a function pointer.
callbackfunc = CALLBACKFUNC(callback)
print("Python ctypes.CFUNCTYPE: " + str(callbackfunc))

# Call the function pointer.
callbackfunc(1)

# Test ctypes.POINTER.
print("Python ctypes.POINTER: " + str(ctypes.POINTER(ctypes.c_int)))

# Test ctypes.pointer.
print("Python ctypes.pointer: " + str(ctypes.pointer
