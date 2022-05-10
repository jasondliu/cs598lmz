import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)
    z = ctypes.c_long(3)

def f(s):
    s.x = 1
    s.y = 2
    s.z = 3

def g(s):
    s.x = 1
    s.y = 2
    s.z = 3

class C(object):
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3

def h(c):
    c.x = 1
    c.y = 2
    c.z = 3

def main():
    s = S()
    f(s)
    g(s)
    c = C()
    h(c)

main()
