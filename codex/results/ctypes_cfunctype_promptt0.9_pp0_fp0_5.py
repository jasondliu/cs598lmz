import ctypes
# Test ctypes.CFUNCTYPE
#################################################################
# define a C function
p = cdll.LoadLibrary('./build/lib/libsay.so')
# get the prototype of the vector add function  
func_type = ctypes.CFUNCTYPE(
    None,             # return type
    ctypes.c_int,     # arg types
    ctypes.c_double, 
    ctypes.c_float,
    ctypes.c_char_p, 
    ctypes.c_void_p) 
# farg1, farg2, sarg, p
# create a ctypes callback
func = func_type(
    lambda iarg1, farg1, farg2, sarg, parg: 
        print("args are: %d %f %f %s %d" %(iarg1, farg1, farg2, sarg, 0)))
# set the callback
p.register_cb(func)
# invoke the callback from C
p.invoke_cb(2, 3.14, 3.14, b"OK")
# cb(2,
