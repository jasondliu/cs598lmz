import ctypes
# Test ctypes.CFUNCTYPE

def f(x):
    return x

F = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f2 = F(f)

print f2(42)

# Test ctypes.c_int.from_param()

def f(x):
    return x

F = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f2 = F(f)

print f2(ctypes.c_int(42))

# Test ctypes.c_char_p.from_param()

def f(x):
    return x

F = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_char_p)
f2 = F(f)

print f2(ctypes.c_char_p("Hello, world"))

# Test ctypes.c_wchar_p.from_param()

def f(x):
    return x

F = ctypes.CFUNCT
