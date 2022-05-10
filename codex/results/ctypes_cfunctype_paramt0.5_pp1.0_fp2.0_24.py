import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(num):
    print("myfunc called with %d" % num)
    return num * 2

f = FUNTYPE(myfunc)
print(f(4))

# The following code is equivalent to the previous example:

def myfunc(num):
    print("myfunc called with %d" % num)
    return num * 2

f = FUNTYPE(myfunc)
print(f(4))

# The following code passes a function pointer to a C function:

def myfunc(num):
    print("myfunc called with %d" % num)
    return num * 2

f = FUNTYPE(myfunc)
lib.call_func(f)

# The following code passes a function pointer to a C function:

def myfunc(num):
    print("myfunc called with %d" % num)
    return num * 2

f = FUNTYPE(myfunc)
lib.call_func(f)

# The following code passes a function pointer to a C function
