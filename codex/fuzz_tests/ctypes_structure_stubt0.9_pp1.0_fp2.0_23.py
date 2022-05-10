import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()
    __slots__ = ['x', 'z']

a = S()
a.x = 1
try: a.y = 2
except AttributeError: pass
else: print('unexpected')
a.z = 3
try: a.w = 4
except AttributeError: pass
else: print('unexpected')
print(a.x, a.z)

# Issue 5551.
class P(ctypes.Structure):
    _fields_ = (
        ("value", ctypes.c_int),
        ("prev", ctypes.POINTER(lambda: P)),
    )

# Issue 9485.
class X(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(ctypes.c_byte))]
assert X.p._type_ == ctypes.c_byte
