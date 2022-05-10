import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def myfunc(n):
    print "myfunc", n
    return n + 1

f = FUNTYPE(myfunc)
f(1)

f = FUNTYPE(lambda n: n + 1)
f(1)

f = FUNTYPE(lambda n: n + 1)
f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1)

#f = FUNTYPE(lambda n: n + 1)
#f(1
