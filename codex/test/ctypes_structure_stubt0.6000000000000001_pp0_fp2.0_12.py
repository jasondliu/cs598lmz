import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)

def get_addr(s):
    return ctypes.addressof(s.x)

def main():
    s = S()
    print("Address of s.x: %d" % get_addr(s))

if __name__ == "__main__":
    main()
