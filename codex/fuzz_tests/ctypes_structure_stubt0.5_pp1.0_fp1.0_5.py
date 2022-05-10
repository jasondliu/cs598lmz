import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

def main():
    s = S()
    print(s.x)
    print(s.y)
    print(s.z)
    print(s.x, s.y, s.z)
    print(s)
    s.x = 100
    s.y = 200
    s.z = 300
    print(s.x)
    print(s.y)
    print(s.z)
    print(s.x, s.y, s.z)
    print(s)
    ss = S(x=100, y=200, z=300)
    print(ss)
    print(s == ss)
    ss = S(x=100, y=200, z=400)
    print(s == ss)

if __name__ == '__main
