import ctypes

class S(ctypes.Structure):
    x = y = z = 0

class u32(ctypes.Union):
    _fields_ = [('_u', ctypes.c_uint),
                ('_s', S)]

def run(n, x):
    """
    >>> run(100000, 12345)
    100000
    """
    u = u32(x)
    for _ in range(n):
        a = u._u
        u._s.x = u._s.y = u._s.z = a
        b = u._s.x
        u._u = b
        u._s.x = u._s.y = u._s.z = b

def main(n):
    run(n, 12345)
    run(n, 54321)

main(int(sys.argv[1]))
