import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int) #Python assumes int is 32bit

def do_something(a, b):
    print "Estoy haciendo algo con", a, b
    return a * b

fun = FUNTYPE(do_something)
print fun(2, 5)
