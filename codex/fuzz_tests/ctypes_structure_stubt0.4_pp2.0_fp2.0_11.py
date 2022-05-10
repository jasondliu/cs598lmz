import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def foo(x):
    print x

def bar(x):
    print x

def baz(x):
    print x

def main():
    s = S()
    s.x = 1
    s.y = 2

    foo(s.x)
    bar(s.y)
    baz(s.x)

main()
