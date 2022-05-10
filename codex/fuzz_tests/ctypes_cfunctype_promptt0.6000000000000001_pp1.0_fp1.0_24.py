import ctypes
# Test ctypes.CFUNCTYPE
def py_callback(name, x, y):
    print "name is", name
    print "x is", x
    print "y is", y
    return x + y

callback_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int)
callback = callback_type(py_callback)

# Test ctypes.c_void_p
class P(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
p = P()
p.x = 1
p.y = 2

# Test ctypes.c_char_p
string = ctypes.c_char_p("abc")

# Test ctypes.c_wchar_p
wstring = ctypes.c_wchar_p(u"abc")

# Test ctypes.c_char
c = ctypes.c_char('a')

# Test ctypes.c_wchar

