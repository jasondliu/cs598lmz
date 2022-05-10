import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def print_field(name):
    print("<{:<10}{:<20}{:<20}>".format(name, repr(getattr(ctypes, name)), str(type(getattr(ctypes, name)))))

if "__main__" == __name__:
    for name in dir(ctypes):
        if name.endswith("_p") or name.endswith("_returns_p"):
            print_field(name)

def test(p):
    if "__main__" != __name__:
        print("before: {}".format(p))
    ctypes.CFuncPtr(p)
    if "__main__" != __name__:
        print("after: {}".format(p))
    return p
