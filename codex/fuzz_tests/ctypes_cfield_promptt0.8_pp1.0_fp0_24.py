import ctypes
# Test ctypes.CField(ctypes.c_struct_CField, "d_ino", 8)

ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2)
ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2, 2, ">h")
ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2, 2, "<h")
ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2, 2, "h")
ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2, 2, "=h")

ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2, 1, ">h")
ctypes.CField(ctypes.c_struct_CField, "d_reclen", 2, 1, "<h")
ctypes.CField(ctypes.c_struct_CField, "d_re
