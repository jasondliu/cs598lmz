import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class Exponent(object):
    def __init__(self, n):
        self.n = n
        self.lib = ctypes.cdll.LoadLibrary("./libexponent.so")
        self.lib.exponent.restype = ctypes.c_double
        self.lib.exponent.argtypes = [ctypes.c_double, ctypes.c_int]

    def __call__(self, x):
        return self.lib.exponent(x, self.n)

    def __str__(self):
        return "x^%d" % self.n


exponent = Exponent(2)
print exponent(2)
print exponent(5)
print exponent

#exponent = Exponent(3)
#print exponent(2)
#print exponent(5)
#print exponent
