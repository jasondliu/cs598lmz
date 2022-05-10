import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(42)
    y = ctypes.c_long(42)

def f():
    s = S()
    s.x = 1
    s.y = 2
    return s

def g():
    s = S()
    s.x = 1
    s.y = 2
    return (s, s)

def h():
    s = S()
    s.x = 1
    s.y = 2
    return (s, s, s)

def i():
    s1 = S()
    s1.x = 1
    s1.y = 2
    s2 = S()
    s2.x = 3
    s2.y = 4
    return (s1, s2)

def j():
    s = S()
    s.x = 1
    s.y = 2
    return (s, s, s, s)

def k():
    s = S()
    s.x = 1
    s.y = 2
    return [s, s, s, s]

