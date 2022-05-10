import ctypes
# Test ctypes.CFUNCTYPE
# Test ctypes.POINTER

ftype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 42

f = ftype(func)

c_func = ctypes.POINTER(ftype)

funcptr = c_func(f)

print(funcptr[0](0))

# Test c_wchar_p

s = "hello"
s = ctypes.c_wchar_p(s)

print(s.value)


# Test c_char_p

s = b"hello"
s = ctypes.c_char_p(s)

print(s.value)

# Test c_void_p

s = b"hello"
