import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def py_add(a, b):
    return a + b

py_add_ptr = FUNTYPE(py_add)
c_add_ptr = FUNTYPE(c_add)

print("c_add(1, 2) = %d" % c_add(1, 2))
print("py_add_ptr(1, 2) = %d" % py_add_ptr(1, 2))
print("c_add_ptr(1, 2) = %d" % c_add_ptr(1, 2))

# ----------------------------------------
print("")
print("[*] ctypes - struct")
print("-------------------")

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class RECT(ctypes.Structure):
    _fields_ = [("upper_left", POINT),
                ("lower_right", POINT)]

rect =
