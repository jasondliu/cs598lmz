import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cmp_func = CMPFUNC(func)
print cmp_func(1, 2)

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

point = POINT(1, 2)
p_point = ctypes.POINTER(POINT)(point)
print p_point.contents

# Test ctypes.c_char_p
s = ctypes.c_char_p('Hello, World')
print s.value

# Test ctypes.c_wchar_p
s = ctypes.c_wchar_p('Hello, World')
print s.value

# Test ctypes.c_void_p
p = ctypes.c_void_p(0)
print
