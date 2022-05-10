import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    ctypes.CField(1)

if __name__ == '__main__':
    main()
