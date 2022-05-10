import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

def f(x):
    return x * x

class C(A):
    def __init__(self):
        A.__init__(self)
        self.f_ = f
        self.x_ = 1

    def f(self, x):
        return self.f_(x)
    
    def x(self):
        return self.x_
    
    def s(self):
        return S(1.0, 2.0)
    
    def ls(self):
        return [S(1.0, 2.0), S(3.0, 4.0)]
    
    def d(self):
        return {"x": 1.0, "y": 2.0}
    
    def ld(self):
        return [{"x": 1.0, "y": 2.0}, {"x": 3.0, "y": 4.0}]

    def _s(self, s):
        print(s.x, s.y)
    
