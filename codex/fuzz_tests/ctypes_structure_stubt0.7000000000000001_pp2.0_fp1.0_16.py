import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(3)
    y = ctypes.c_long(4)
    z = ctypes.c_long(5)
class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_long),
                ("b", ctypes.c_long),
                ("c", ctypes.c_long)]

def test(s):
    print(s, s.x, s.y)

s = S()
print(s, s.x, s.y)
d = D()
print(d, d.a, d.b, d.c)

test(s)
test(d)
