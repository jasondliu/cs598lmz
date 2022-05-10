import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))

def foo(x):
    print "foo(%d)" % (x.contents.value,)

f = FUNTYPE(foo)

x = ctypes.c_int(42)
f(ctypes.pointer(x))
</code>

