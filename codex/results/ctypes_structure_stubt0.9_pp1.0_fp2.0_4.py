import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    pass

def S0() -> S:
    a = S()
    return a

def S1(a: S) -> int:
    return 0

def main():
    a = S()
    b = S0()
    print(a == b)

if __name__ == '__main__':
    main()
