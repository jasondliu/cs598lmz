fn = lambda: None
# Test fn.__code__

class A:
    def __init__(self, x):
        self.x = x
    def f(self):
        return self.x

def f(x):
    return x

def g(x, y):
    return x + y

def h(x, y, z):
    return x + y + z

def i(x, y, z, u):
    return x + y + z + u

def j(x, y, z, u, v):
    return x + y + z + u + v

def k(x, y, z, u, v, w):
    return x + y + z + u + v + w

def l(x, y, z, u, v, w, t):
    return x + y + z + u + v + w + t

def m(x, y, z, u, v, w, t, s):
    return x + y + z + u + v + w + t + s

def n(x, y, z, u, v, w, t,
