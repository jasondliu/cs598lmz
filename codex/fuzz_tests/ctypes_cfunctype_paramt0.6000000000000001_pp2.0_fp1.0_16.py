import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print('callback called with {}'.format(x))

# cast the callback to a C function type
CMPFUNC = FUNTYPE(callback)

# call the callback
CMPFUNC(42)
</code>
The documentation for <code>ctypes</code> is here. 

