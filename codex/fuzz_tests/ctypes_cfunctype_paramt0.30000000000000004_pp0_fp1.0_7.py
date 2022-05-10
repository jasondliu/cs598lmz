import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print("myfunc({0}, {1})".format(a, b))
    return a + b

myfunc_c = FUNTYPE(myfunc)
print("myfunc_c(2, 3) = {0}".format(myfunc_c(2, 3)))

# Callback function
def myfunc_cb(a, b, cb):
    print("myfunc_cb({0}, {1}, {2})".format(a, b, cb))
    return cb(a, b)

myfunc_cb_c = FUNTYPE(myfunc_cb)
print("myfunc_cb_c(2, 3, myfunc_c) = {0}".format(myfunc_cb_c(2, 3, myfunc_c)))

# Callback function with lambda
myfunc_cb_c = FUNTYPE(myfunc_cb)
print("myfunc_cb_c(2, 3, lambda a, b
