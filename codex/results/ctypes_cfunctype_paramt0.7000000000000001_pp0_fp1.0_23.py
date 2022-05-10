import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
def foo(p):
    print("foo({})".format(p[0]))
    return 42
f = FUNTYPE(foo)
print("callback returned {}".format(f((ctypes.c_int * 1)(4))))
</code>


A:

I think you should try to give the function a pointer to the int that you want to change.
Something like this:
<code>FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))
def foo(p):
    print("foo({})".format(p[0]))
    p[0] = 42
f = FUNTYPE(foo)
c = ctypes.c_int(0)
print("callback returned {}".format(f(ctypes.byref(c))))
print("c is now %d" % c.value)
</code>

