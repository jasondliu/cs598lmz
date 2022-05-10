import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class TC(type(S)):
    def __new__(meta, name, bases, ns):
        res = type(S).__new__(meta, name, bases, ns)
        return res

    def __get__(self, instance, owner):
        if instance == 10:
            return 0
        elif instance == 20:
            return -1
        elif instance == 30:
            return S()
        elif instance == 40:
            raise AttributeError
        else:
            return type(S).__get__(self, instance, owner)

class Test(metaclass=TC):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

class X(Test):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('a',
