import ctypes
# Test ctypes.CFUNCTYPE(None)
def callback():
    print("callback")
CALLBACK = ctypes.CFUNCTYPE(None)
callback = CALLBACK(callback)
callback()

# Test ctypes.CFUNCTYPE(ctypes.c_int)
def callback(i):
    print("callback")
    return i + 1
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
callback = CALLBACK(callback)
print(callback(1))

# Test ctypes.CFUNCTYPE(None, ctypes.c_int)
def callback(i):
    print("callback")
CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int)
callback = CALLBACK(callback)
callback(1)

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def callback(i, j):
    print("callback")
    return i + j
CALLBACK = ctypes.CFUN
