import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_longlong)

def cfunc():
    return True

print 's', FUNTYPE(cfunc)

def f(k):
    print 'call f'
    return k

print 's', FUNTYPE(f)

# callback = FUNTYPE(lambda x: x*2)
# callback(2)
