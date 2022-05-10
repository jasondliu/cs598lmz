import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint
    _fields_ = [
        ('x', ctypes.c_uint),
        ('b', ctypes.c_char)
    ]

def test_sizeof():
    assert ctypes.sizeof(S) == 5

def test_access():
    s = S()
    print(s.x)
    s.x =  1
    print(s.x)
    print(s.b)
    s.b =  1
    print(s.b)

# test_sizeof()

test_access()
