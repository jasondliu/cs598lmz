import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int, # returns int
    ctypes.c_int, # first arg is an int
    ctypes.c_double, # second arg is a double
    ctypes.c_void_p # third arg is a void*
)

def test_func(x,y,z):
    print("x=%s"%x)
    print("y=%s"%y)
    print("z=%s"%z)
    return x+y

f = FUNTYPE(test_func)

n=f(2,3.14,None)

print("n=%s"%n)
