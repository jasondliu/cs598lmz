import ctypes
# Test ctypes.CFUNCTYPE
def f(x):
    return x

f_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f_t(f)

# Test ctypes.POINTER
def f_ptr(x):
    return x

f_ptr_t = ctypes.POINTER(f_t)
f_ptr_t(f_ptr)


# Test ctypes.c_int.in_dll
ctypes.c_int.in_dll(ctypes.cdll.msvcrt, '_errno')

# Test ctypes.c_int.from_address
ctypes.c_int.from_address(ctypes.addressof(ctypes.c_int.in_dll(ctypes.cdll.msvcrt, '_errno')))

# Test ctypes.c_int.value
ctypes.c_int.in_dll(ctypes.cdll.msvcrt, '_errno').value

# Test ctypes.c_int.value =
ct
