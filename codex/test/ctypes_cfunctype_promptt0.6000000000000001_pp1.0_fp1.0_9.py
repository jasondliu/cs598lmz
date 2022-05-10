import ctypes
# Test ctypes.CFUNCTYPE

def my_func(x):
    print("my_func() called with argument: " + str(x))
    return x*2

my_func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(my_func)

print("my_func_ptr.argtypes: " + str(my_func_ptr.argtypes))
print("my_func_ptr.restype: " + str(my_func_ptr.restype))

print("Calling my_func_ptr(11): " + str(my_func_ptr(11)))

print("Done!")
