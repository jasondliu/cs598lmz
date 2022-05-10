import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

dll.fun=FUNTYPE(fun)

# c_int, c_char_p, c_void_p, c_double, c_bool
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
@FUNTYPE
def fun(name):
    print("hi", name.decode("utf-8"))
    return 42

dll.fun=FUNTYPE(fun)

# STRING
dll.get_string.restype = ctypes.c_char_p
dll.get_string.argtypes = None
s = dll.get_string()
print(s)

# PRINT
dll.print_int.argtypes = [ctypes.c_int]
dll.print_int.restype = None
for i in range(10):
    dll.print_int(i)

# MULTI
dll.multi.argtypes = [ctypes.c_int, ctypes.c_int]
dll.multi.restype = ctypes.c_
