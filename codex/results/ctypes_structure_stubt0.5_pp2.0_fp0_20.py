import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p

def f():
    return S()

def main():
    print f().x

if __name__ == '__main__':
    main()
