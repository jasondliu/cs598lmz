import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func_c = func_type(func)

print(func_c(1, 2))

# Test ctypes.POINTER
def func_pointer(a, b):
    return a + b

func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
func_c = func_type(func_pointer)

a = ctypes.c_int(1)
b = ctypes.c_int(2)
print(func_c(ctypes.byref(a), ctypes.byref(b)))

# Test ctypes.c_char_p
def func_char_p(a, b):
    return a + b

