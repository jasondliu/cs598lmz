import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_ulonglong

s = S()
s.x = 42
s.y = 42

# this fails because ctypes.c_longlong and ctypes.c_ulonglong
# have the same typecode
assert s.x == s.y

# this fails because ctypes.c_longlong and ctypes.c_ulonglong
# have the same typecode
assert s.x &lt; s.y

# this works
assert s.x &lt; ctypes.c_ulonglong(s.y).value
</code>

