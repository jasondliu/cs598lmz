import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f():
    a = S()
    b = S()
    c = S()
    a.x = 0
    a.y = 1
    b.x = 2
    b.y = 3
    c.x = 4
    c.y = 5
    return a, b, c

def main():
    a, b, c = f()
