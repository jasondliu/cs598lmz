import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
class ODE_Solver:
    def __init__(self, f, x0, y0, h, n):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.n = n
        self.x = [0] * (n + 1)
        self.y = [0] * (n + 1)
        self.x[0] = x0
        self.y[0] = y0

    def solve(self):
        for i in range(1, self.n + 1):
            self.x[i] = self.x[i - 1] + self.h
            self.y[i] = self.y[i - 1] + self.h * self.f(self.x[i - 1], self.y[i - 1])
        return self.x, self
