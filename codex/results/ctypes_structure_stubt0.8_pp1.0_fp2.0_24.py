import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    __slots__ = []

class C:
    __slots__ = ["a", "x"]
    def __init__(self, a):
        self.a = a

    def __getattr__(self, name):
        if name == "x":
            return S()
        raise AttributeError

C(42).x.x = 3.14
