import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)
f = FUNTYPE(lambda x,y: x+y)
print(f(1,2))
</code>
<code>3
</code>

