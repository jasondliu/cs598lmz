import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(func)

print(cmp_func(1, 2))

# Test ctypes.POINTER
class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

Point = ctypes.POINTER(POINT)

p = Point()
p.contents = POINT(1, 2)

print(p.contents.x, p.contents.y)

# Test ctypes.c_char_p
s = ctypes.c_char_p(b'hello world')
print(s.value)

# Test ctypes.c_wchar_p
s = ctypes.c_wchar_p('你好')
print(s.value)

# Test ctypes.
