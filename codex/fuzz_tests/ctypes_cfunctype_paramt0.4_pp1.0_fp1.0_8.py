import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def c_callback(a,b):
    print(a,b)
    return a+b

def c_callback2(a,b):
    print(a,b)
    return a*b

# callbacks = [FUNTYPE(c_callback),FUNTYPE(c_callback2)]
callbacks = []

# lib = ctypes.CDLL('./libcallbacks.so')
lib = ctypes.CDLL('./libcallbacks.dylib')

lib.register_callback(FUNTYPE(c_callback))
lib.register_callback(FUNTYPE(c_callback2))

lib.call_callbacks(1,2)
