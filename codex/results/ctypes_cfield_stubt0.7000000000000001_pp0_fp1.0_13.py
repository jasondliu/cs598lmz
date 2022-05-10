import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
