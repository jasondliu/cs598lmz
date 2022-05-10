import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    print "myfunc", n
    return n+1

f = FUNTYPE(myfunc)
print f(1)

f = FUNTYPE(lambda n: n+1)
print f(2)

f = FUNTYPE(lambda n: n+1, use_errno=True)
print f(3)

f = FUNTYPE(lambda n: n+1, use_last_error=True)
print f(4)

f = FUNTYPE(lambda n: n+1, use_last_error=True, use_errno=True)
print f(5)

f = FUNTYPE(lambda n: n+1, use_errno=True, use_last_error=True)
print f(6)

#f = FUNTYPE(lambda n: n+1, use_errno=True, use_last_error=True,
#                          calling_convention='win')
#print f(7)

f = FUNTYPE(lambda n:
