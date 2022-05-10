import ctypes
# Test ctypes.CFUNCTYPE

# Function prototype for first callback
CALLBACK_FUNC =  ctypes.CFUNCTYPE(None, ctypes.c_int)

def pycallback(val):
    print("pycallback(%r)" % val)

myvariant = ctypes.c_int(42)

