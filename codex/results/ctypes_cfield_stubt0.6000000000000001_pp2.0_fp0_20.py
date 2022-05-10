import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFuncPtr = type(S.x.__add__)

class C(object):
    """
    A class that can be used for testing ctypes attributes
    """

    def __init__(self):
        self.i = 1
        self.s = "Hello World"
        self.d = {"a": 1, "b": 2}
        self.f = 3.14
        self.l = [1, 2, 3]
        self.t = (1, 2, 3)
        self.b = False
        self.n = None
        self.x = S()

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return True

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
