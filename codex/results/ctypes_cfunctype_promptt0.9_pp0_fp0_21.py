import ctypes
# Test ctypes.CFUNCTYPE arguments

class TP(tuple):
    pass

##clong = ctypes.c_long
##clongp = ctypes.POINTER(clong)
##
##ll = list(range(10))
##la = (clong * len(ll))(*ll)
##
##x = clong()
##
##def func(arr):
##    x = clong()
##    array_length = arr._length_
##    array_ptr = arr._ptr_
##    ptr = clongp()
##    ptr.contents = clong(array_ptr)
##    cfunc = ctypes._CFuncPtr(None, ctypes.c_long, [clongp, clong])
##    ctypes.call_function(cfunc, (ptr, ctypes.c_long(array_length), x))
##    print x.value
##
##func(la)
