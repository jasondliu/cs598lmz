import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int64()


def f():
    return S()

import pypyjit

if __name__ == '__main__':
    pypyjit.set_param(threshold=10000)
    for i in range(50000):
        s = f()
        s.x **= 3
