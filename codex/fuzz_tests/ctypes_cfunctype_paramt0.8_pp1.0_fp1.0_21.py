import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

def foo(a):
    return a

func = FUNTYPE(foo)

print func(32)
</code>
which gives me:
<code>$ python test_c.py
32
</code>

