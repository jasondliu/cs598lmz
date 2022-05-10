import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class D(S):
    y = ctypes.c_int

class E(D):
    z = ctypes.c_int

def main():
    print(ctypes.sizeof(S))
    print(ctypes.sizeof(D))
    print(ctypes.sizeof(E))

main()
