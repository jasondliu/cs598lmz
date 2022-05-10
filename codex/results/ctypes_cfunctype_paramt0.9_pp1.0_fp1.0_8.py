import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
bind = ctypes.CDLL(libfile)
def c_wrapper(fun):
    def wrapp(*args, **kwargs):
        return fun(*args, **kwargs)
    return wrapp

sum = bind.sum_ints
sum.argtypes = [ctypes.c_int, ctypes.c_int] 
sum.restype = ctypes.c_int

print(sum(32,16)) # 48

my_fun = FUNTYPE(lambda x: x + 1)
print(my_fun(12)) # 13
</code>

If the functions you call have floating point arguments, the <code>c_double</code> type can be used instead of <code>c_int</code>. Like this
<code>from ctypes import *
sum = bind.sum_doubles
sum.argtypes = [c_double, c_double] 
sum.restype = c_double
</code>

Much of the code can be made generic by defining a set of wrapper functions like this

