import ctypes
# Test ctypes.CField
p = ctypes.c_char_p("Hello")
if ctypes.cast(p, ctypes.c_void_p).value != ctypes.addressof(p):
    raise Exception("could not cast a pointer to void")

# Test ctypes.CField.from_param
def f(p):
    return ctypes.cast(p, ctypes.c_void_p).value
class X(ctypes.Structure):
    _fields_ = [("p", ctypes.c_char_p)]
x = X("Hello")
if f(x.p) == ctypes.addressof(x):
    raise Exception("from_param method not used")

# Test ctypes.CField.from_address
class Y(ctypes.Structure):
    _fields_ = [("p", ctypes.c_char_p)]
y = Y(ctypes.addressof(p))
if y.p != p:
    raise Exception("from_address method not used")
