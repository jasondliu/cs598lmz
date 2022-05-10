import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    print (a, b)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

lib.set_callback(CALLBACK(my_callback))

lib.invoke_callback(1, 2)

# Test byref() and pointers
#int my_sum(int arg1, int arg2, int *sum)
my_sum = lib.my_sum
my_sum.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
my_sum.restype = ctypes.c_int

a = ctypes.c_int(1)
b = ctypes.c_int(2)
s = ctypes.c_int(0)
ret = my_sum(a, b, ctypes.byref(s))
print(ret, s.value)
