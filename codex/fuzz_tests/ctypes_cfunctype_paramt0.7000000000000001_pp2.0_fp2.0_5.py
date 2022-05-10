import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Add comment
def f(x):
    return x + 1

cfunc = FUNTYPE(f)
print cfunc(1, 2)

# Add comment
class T(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int)
    ]

def f2(x):
    print x.contents
    x.contents.x += 1
    return 0

cfunc2 = FUNTYPE(f2)
t = T()
t.x = 10
print 't=', t.x
cfunc2(ctypes.pointer(t))
print 't=', t.x
</code>


A:

I'm not a ctypes expert, but it looks like <code>f2</code> is executed within the context of the calling function, which is <code>gdb.execute</code>. The <code>gdb.execute</code> command only returns after the execution of the inferior command completes and control returns to g
