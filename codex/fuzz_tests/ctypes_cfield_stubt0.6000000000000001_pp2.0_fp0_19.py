import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            return self.b[key]
    def __setattr__(self, key, value):
        self.__dict__[key] = value

def to(c):
    c.x = c.x.value
    return c

def from_(c):
    c.x = ctypes.c_int(c.x)
    return c

def test():
    s = S(42)
    c = C(s, None)
    c.x = 37
    assert s.x == 37
    try:
        c.y = 37
    except AttributeError:
        pass
    else:
        raise Exception("did not raise")

if __name__ == '__main__':
    test()
