import ctypes

class S(ctypes.Structure):
    x = property(lambda self: self._x)
    def __getattr__(self, name):
        if name == 'x':
            return self._x

class D(S):
    def __init__(self, x):
        self._x = x

class E(S):
    def __init__(self):
        self._x = 42

class F(S):
    def __init__(self):
        self._x = 42
el = E()

el.y = 420
print(el.y)

el2 = F()
print(el2.y)
