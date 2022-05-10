import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def main():
    s = S()
    s.x = 5
    print(s.x)
    print(ctypes.CField)

if __name__ == '__main__':
    main()
</code>

