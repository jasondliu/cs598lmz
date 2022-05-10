import ctypes
# Test ctypes.CFUNCTYPE
c_double_p = ctypes.POINTER(ctypes.c_double)
c_double2_t = ctypes.CFUNCTYPE(ctypes.c_double,
                               ctypes.c_double, ctypes.c_double)

print("Testing ctypes.CFUNCTYPE")
for i in range(10):
    f = c_double2_t(lambda x, y: x * y)
