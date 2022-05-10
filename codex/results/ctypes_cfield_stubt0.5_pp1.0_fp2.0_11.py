import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    x = S.x
    print(x)
    print(type(x))
    print(type(x) is ctypes.CField)
    print(type(x) is ctypes.Field)
    print(type(x) is ctypes.Field)

if __name__ == '__main__':
    main()
