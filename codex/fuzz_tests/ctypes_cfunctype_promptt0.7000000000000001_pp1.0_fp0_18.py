import ctypes
# Test ctypes.CFUNCTYPE
def func_ptr(x):
    return x + 1
func_ptr_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func = func_ptr_type(func_ptr)
print func(1)

# Test ctypes.POINTER
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

ptr_type = ctypes.POINTER(Point)
ptr = ptr_type()
ptr.contents.x = 1
ptr.contents.y = 2
print ptr.contents.x, ptr.contents.y

# Test ctypes.byref
def func_by_ref(x):
    x.value = x.value + 1
x = ctypes.c_int(1)
func_by_ref(ctypes.byref(x))
print x.value

# Test ctypes.c_char_p
s = ctypes.c_char_p("Hello, World")
