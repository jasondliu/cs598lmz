import ctypes

class S(ctypes.Structure):
    x = True
    y = True
    z = True

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def test():
    s = S()
    s.x = f(s.x)
    s.y = g(s.y)
    s.z = h(s.z)
    return s

def main():
    for i in range(100000):
        s = test()
        if not s.x and not s.y and not s.z:
            return 1
    return 0

print main()
