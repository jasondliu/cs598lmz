import ctypes
# Test ctypes.CFUNCTYPE
def func(arg):
    return arg

CFUNCTYPE(c_int)(func)(42)

# Test ctypes.POINTER
class POINTER(object):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return '<POINTER>'
    def contents(self):
        return self.x
    def __eq__(self, other):
        return self.x == other.x

POINTER(42)

# Test ctypes.c_void_p
c_void_p(42)

# Test ctypes.string_at
string_at(c_char_p(b"hello"))
string_at(c_wchar_p(u"hello"))

# Test ctypes.wstring_at
wstring_at(c_wchar_p(u"hello"))

# Test ctypes.addressof
addressof(c_int(42))

# Test ctypes.byref
byref(c_int(42))

# Test c
