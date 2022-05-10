import ctypes
# Test ctypes.CFUNCTYPE()

PCT = ctypes.POINTER(ctypes.c_int)
FPT = ctypes.CFUNCTYPE(PCT)

def fn1():
    print 'fn1 called'
    return 42

def fn2():
    print 'fn2 called'
    return 24

f1 = FPT(fn1)
f2 = FPT(fn2)

print f1(), f2()
