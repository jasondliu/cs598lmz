import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    s = S()
    s.x = 42
    print(s.x)

if __name__ == '__main__':
    main()
