import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields = [('x', ctypes.c_int),
               ('y', ctypes.c_int)]

def main():
    s = S()
    s.x = 10
    s.y = 20
    print(s.x, s.y)

if __name__ == '__main__':
    main()
