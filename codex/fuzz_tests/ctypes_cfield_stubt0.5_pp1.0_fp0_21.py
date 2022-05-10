import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    print(type(S.x))
    print(type(ctypes.CField))

if __name__ == '__main__':
    main()
