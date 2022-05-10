import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def f(i):
    return i + 1

CALLBACK = FUNTYPE(f)

print CALLBACK(1)
</code>
The output is <code>2</code>.

