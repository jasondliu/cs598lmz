import ctypes
# Test ctypes.CFUNCTYPE()
int_p = ctypes.POINTER(ctypes.c_int)
print(int_p)
# <class 'ctypes.LP_c_int'>
# Test ctypes.POINTER(ctypes.c_int)

# Test ctypes.c_int()
print(ctypes.c_int())
# 0

# Test ctypes.c_int(1)
print(ctypes.c_int(1))
# c_long(1)

# Test ctypes.byref()
print(ctypes.byref(ctypes.c_int(1)))
# <ctypes.LP_c_long object at 0x7f8b834e0530>

# Test ctypes.addressof()
print(ctypes.addressof(ctypes.c_int(1)))
# 140308475506888

# Test ctypes.pointer()
print(ctypes.pointer(ctypes.c_int(1)))
# <ctypes.LP_c_long object at 0x7f8b834e04d
