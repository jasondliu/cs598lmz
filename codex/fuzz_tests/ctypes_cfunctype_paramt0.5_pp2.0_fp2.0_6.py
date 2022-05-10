import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

f = FUNTYPE(myfunc)
print f(2, 3)

# callbacks
def callback(a, b):
    print "callback called with", a, b

f = FUNTYPE(callback)
f(1, 2)

# callbacks with return values
def callback(a, b):
    print "callback called with", a, b
    return a + b

f = FUNTYPE(callback)
print f(1, 2)

# callbacks with ctypes arguments
def callback(a, b):
    print "callback called with", a, b
    return a + b

f = FUNTYPE(callback)
print f(ctypes.c_int(1), ctypes.c_int(2))

# callbacks with ctypes arguments and return values
def callback(a, b):
    print "callback called with", a, b
    return a + b

f = FUNTYPE(callback
