import ctypes
# Test ctypes.CField

libc = CDLL(NUL)

class S(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", c_int),
        ("c", c_int),
        ("d", c_int),
        ("e", c_int),
        ("f", c_int),
        ("g", c_int),
        ("h", c_int),
        ("i", c_int),
        ("j", c_int),
    ]

class T(Structure):
    _fields_ = [
        ("a", c_int),
        ("b", S),
        ("c", c_int),
    ]

assert sizeof(S) == 40
assert sizeof(T) == 48

# test ints
s = S()
assert s.a == 0
assert s.b == 0
assert s.c == 0
assert s.d == 0
assert s.e == 0
assert s.f == 0
assert s.g == 0
assert s.h == 0
assert s.i == 0
assert s
