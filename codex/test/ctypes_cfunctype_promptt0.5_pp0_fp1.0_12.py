import ctypes
# Test ctypes.CFUNCTYPE callback
def callback(value):
    print('Called back with value', value)

CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# Create an instance of CALLBACKFUNC
c_callback = CALLBACKFUNC(callback)
