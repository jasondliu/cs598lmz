import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    for item in [ctypes.c_int, ctypes.c_int()]:
        print type(item)
    for item in [S, S()]:
        print type(item)
    for item in [S.x, S().x]:
        print type(item)

def main():
    test()

if __name__ == '__main__':
    main()
