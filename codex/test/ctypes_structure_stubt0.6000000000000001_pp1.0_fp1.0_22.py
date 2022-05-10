import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    if x:
        s = S()
    else:
        s = S()
    return s

def g(x):
    s = f(x)
    return s.x

def main(n):
    for i in xrange(n):
        g(i & 1)

def target(*args):
    return main, None

if __name__ == "__main__":
    import sys
