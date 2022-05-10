import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def myfunc(a,b):
    print("myfunc({},{})".format(a,b))
    return a*b

f = FUNTYPE(myfunc)
print(f(2,3))
</code>
This is the output:
<code>myfunc(2,3)
6
</code>

