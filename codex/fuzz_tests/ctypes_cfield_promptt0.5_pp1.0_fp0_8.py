import ctypes
# Test ctypes.CField class

import ctypes

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char)]

s = S()
print(s.a)
print(s.b)

t = T()
print(t.s.a)
print(t.s.b)
print(t.c)

# This fails, because the structure is not initialized
#print(t.s.a.__class__)

# This fails because the structure is not initialized
#print(t.s.a.value)

# This fails because the structure is not initialized
#t.s.a = "abc"

# This fails because the structure is not initialized
#t.s.a = 1

# This works
t.s.a = ctypes.c_int(1)

# This works
t.s.a =
