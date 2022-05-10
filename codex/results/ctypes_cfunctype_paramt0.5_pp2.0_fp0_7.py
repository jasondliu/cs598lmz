import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

import numpy as np

class MySolver(Solver):
    def __init__(self, a, b, f, n, method, eps):
        super(MySolver, self).__init__(a, b, f, n, method, eps)

    def solve(self):
        if self.method == 'euler':
            return self.euler(self.a, self.b, self.f, self.n, self.eps)
        elif self.method == 'runge-kutta':
            return self.runge_kutta(self.a, self.b, self.f, self.n, self.eps)
        elif self.method == 'adams':
            return self.adams(self.a, self.b, self.f, self.n, self.eps)

    def euler(self, a, b, f, n, eps):
        x = np.linspace(a, b, n)
