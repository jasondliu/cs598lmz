import ctypes

class S(ctypes.Structure):
    x = 1

def f():
    S.x = 2

def main():
    f()
    assert S.x == 2
    return 0

main()
