import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_void_p,ctypes.c_void_p,ctypes.c_void_p)
def f(x,y,z):
    print(x,y,z)
    return 1

#CALLBACK = FUNTYPE( f )
#CALLBACK = FUNTYPE(lambda x,y,z: print(x,y,z))

CALLBACK = FUNTYPE(print)

CALLBACK(0,1,2)

f = CALLBACK
f(0,1,2)
</code>

