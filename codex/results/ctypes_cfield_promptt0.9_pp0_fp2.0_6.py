import ctypes
# Test ctypes.CField_Type()
class CFOOBJ:
    _fields_ = [
        ("A", ctypes.c_char),
        ("B", ctypes.c_int),
        ("C", ctypes.c_int)]

foo = CFOOBJ()
print(foo)
#ctypeze.CFieldType()
# Test ctypeze.CField_Type()
class PFOOBJ:
    _fields_ = [
    ("ONE", ctypeze.CField_Type(ctypes.POINTER(ctypes.c_char), 0)),
    ("TWO", ctypeze.CField_Type(ctypeze.CFUNC_TYPE(ctypes.c_int), 1)),
    ("THREE", ctypeze.CField_Type(ctypes.c_int, 2))]


# Test ctypeze.VTable
class VTO:
    _fields_ = [
        ("a", ctypes.c_char),
        ("b", ctypes.c_char)]

def c_vtable_func(self):
    return 42

def
