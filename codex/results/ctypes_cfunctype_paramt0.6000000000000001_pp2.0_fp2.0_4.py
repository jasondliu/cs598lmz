import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

import numpy as np

class Function(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        return self.function(*args)

    def __add__(self, other):
        def add(*args):
            return self.function(*args) + other(*args)
        return Function(add)

    def __radd__(self, other):
        def radd(*args):
            return other(*args) + self.function(*args)
        return Function(radd)

    def __mul__(self, other):
        def mul(*args):
            return self.function(*args) * other(*args)
        return Function(mul)

    def __rmul__(self, other):
        def rmul(*args):
            return other(*args) * self.function(*args)
        return Function(rmul)

    def __sub__(self, other):
        def sub(*args):
            return self.function
