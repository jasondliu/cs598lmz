import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

o = S()
print o
print repr(o)

print ctypes.ArgumentError(S, "x")
print repr(ctypes.ArgumentError(S, "x"))

a = ctypes.c_char_p("hello")
print a
print repr(a)

print ctypes.ArgumentError(ctypes.c_char_p, "hello")
print repr(ctypes.ArgumentError(ctypes.c_char_p, "hello"))

a = ctypes.c_char_p(None)
print a
print repr(a)

print ctypes.ArgumentError(ctypes.c_char_p, None)
print repr(ctypes.ArgumentError(ctypes.c_char_p, None))
