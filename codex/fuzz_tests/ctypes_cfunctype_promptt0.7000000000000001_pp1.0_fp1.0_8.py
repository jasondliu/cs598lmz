import ctypes
# Test ctypes.CFUNCTYPE
def func_pointer_callback(n):
    print (n)

# initialize the function pointer
f = ctypes.CFUNCTYPE(None, ctypes.c_int)(func_pointer_callback)

# invoke the callback
f(1)

# Test ctypes.POINTER
def func_pointer_callback_2(n):
    print (n)

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(func_pointer_callback_2)
print (f)

# create a pointer object
ptr_obj = ctypes.POINTER(ctypes.c_int)()
# invoke the callback
f(ptr_obj)


# Test global function pointer
def func_pointer_callback_3(n):
    print (n)

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(func_pointer_callback_3)
print (f)

# create a pointer object
ptr_obj = ctypes.POINTER(ctypes.c_int)()
# invoke the callback
f =
