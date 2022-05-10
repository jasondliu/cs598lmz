import ctypes
# Test ctypes.CFUNCTYPE
def foo(a, b, c):
    return a + b + c

def callback(a, b, c):
    print("callback called")
    return a + b + c

# Create a callback function prototype
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create a callback function
mycallback = CALLBACKFUNC(callback)

# Call foo with mycallback as the callback function
