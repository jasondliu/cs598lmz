import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32

def main():
    s = S()
    s.x = 1
    s.y = 2

    s2 = S()
    s2.x = 3
    s2.y = 4

    print(s.x, s.y)
    print(s2.x, s2.y)

    s3 = s + s2

    print(s3.x, s3.y)

