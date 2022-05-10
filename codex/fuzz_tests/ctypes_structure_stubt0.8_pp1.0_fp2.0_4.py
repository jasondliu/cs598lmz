import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class S2(S):
    pass

class F(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", S)
    ]

class F2(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", S2)
    ]

def main():
    a = F()
    a.a = 1
    a.b = 2
    a.c.x = 3
    a.c.y = 4

    A = F2().from_address(ctypes.addressof(a))
    A.c.x = 5
    A.c.y = 6

    print(a.a,a.b,a.c.x,a.c.y)

    # b = F().from_address(ctypes.addressof
