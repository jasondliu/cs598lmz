import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    print(a, b)

CFUNCTYPE(None, c_int, c_int)(func)

# Test ctypes.POINTER
POINTER(c_int)

# Test ctypes.byref
c_int()
byref(c_int())

# Test ctypes.addressof
addressof(c_int())

# Test ctypes.sizeof
sizeof(c_int)

# Test ctypes.cast
cast(c_int(1), POINTER(c_int))

# Test ctypes.string_at
string_at(c_char_p(b"123"), 3)

# Test ctypes.wstring_at
wstring_at(c_wchar_p(u"123"), 3)

# Test ctypes.memset
memset(c_int(), 0, 1)

# Test ctypes.memmove
memmove(c_int(), c_int(), 1)

# Test ctypes.memset
memset(c_int(), 0,
