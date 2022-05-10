import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1, 2, 3)

a = fun()
print type(a)
print a
print a[0], a[1], a[2]
print len(a)

for i in a:
    print i,
print

def fun():
    return []

a = fun()
print type(a)
print a

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@FUNTYPE
def fun():
    return (1, 2, 3)

a = fun()
print type(a)
print a

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(*args):
    return args

a = fun(1, 2, 3)
print type(a)
print a
print a[0], a[1], a[2]

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(*args):
    return args

a = fun(1, 2, 3)
print
