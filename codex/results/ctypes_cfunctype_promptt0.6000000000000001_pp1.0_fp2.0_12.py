import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)

@ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)
def my_callback(x):
    print("my_callback got:", x)
    return x

# Test ctypes.CFUNCTYPE(None, ctypes.c_int32)

@ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)
def my_callback(x):
    print("my_callback got:", x)
    return x

# Test ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_int32)

@ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32)
def my_callback(x):
    print("my_callback got:", x)
    return x

# Test ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_int32
