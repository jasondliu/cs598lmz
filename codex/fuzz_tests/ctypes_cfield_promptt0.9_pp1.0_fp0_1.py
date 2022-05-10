import ctypes
# Test ctypes.CField
ctypes.c_struct_anon_1._fields_ = [("x", ctypes.c_int),
                                   ("y", ctypes.c_int),
                                   ("array", ctypes.c_int * 3)]
data = ctypes.c_struct_anon_1(3, 4, (5, 6, 7))
print("data.x", data.x)
print("data.y", data.y)
for i in range(0, 3):
    print("data.array[%d]" % i, data.array[i])
