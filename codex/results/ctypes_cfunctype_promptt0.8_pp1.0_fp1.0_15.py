import ctypes
# Test ctypes.CFUNCTYPE
def func1(a, b):
    print a, b
ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_double)(func1)(1, 2.3)

# Test ctypes.POINTER
int_ptr = ctypes.POINTER(ctypes.c_int)
int_ptr(ctypes.c_int(5))

# Test ctypes.Structure
class MyStructure(ctypes.Structure):
    _fields_ = [("field1", ctypes.c_int),
                ("field2", ctypes.c_char)]
my_struct = MyStructure(1, "2")

# Test ctypes.Union
class MyUnion(ctypes.Union):
    _fields_ = [("field1", ctypes.c_int),
                ("field2", ctypes.c_char)]
my_union = MyUnion(field1=1)

# Test ctypes.WINFUNCTYPE
def func2(a, b):
    print a, b
ctypes.WINFUNCTYPE
