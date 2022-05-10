import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    def __init__(self, x, y):
        self.x = x
        self.y = y


# TODO check that python dicts are not allowed to have non-hashable elements
