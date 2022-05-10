import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p

s = S()
s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"

s.x = b"w00t"
assert s.x == b"w00t"


