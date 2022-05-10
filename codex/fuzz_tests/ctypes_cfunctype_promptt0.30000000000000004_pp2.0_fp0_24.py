import ctypes
# Test ctypes.CFUNCTYPE(None)
def callback():
    print("callback")
CALLBACK = ctypes.CFUNCTYPE(None)
callback = CALLBACK(callback)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(arg1, arg2):
    print("callback", arg1, arg2)
    return arg1 + arg2
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
callback = CALLBACK(callback)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
def callback(arg1, arg2):
    print("callback", arg1, arg2[0])
    return arg1 + arg2[0]
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
callback
