import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short(1)
    y = ctypes.c_short(2)
    z = ctypes.c_double(3.5)

class T(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int, 1),
        ("b", ctypes.c_int, 2),
        ("c", ctypes.c_int, 3),
    ]

if __name__ == '__main__':
    s = S()
    print(s.x)
    print(s.y)
    print(s.z)
    print(s.x.__class__, s.x.value)
    print(s.y.__class__, s.y.value)
    print(s.z.__class__, s.z.value)
    print(s.x.__class__.__base__, s.x.__class__.__base__.__base__)
