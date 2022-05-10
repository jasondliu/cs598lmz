from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')

class C(object):
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

class D(C):
    __slots__ = ('z',)
    def __init__(self, x, y, z):
        C.__init__(self, x, y)
        self.z = z

def f(x):
    return x is None

def g(x):
    if x:
        return False
    else:
        return True

def h(x):
    if x:
        return False
    else:
        return True

def i(x):
    if x:
        return False
    else:
        return True

def j(x):
    if x:
        return False
    else:
        return True

def k(x, y):
    return x and y

def m(x, y):
    if not x:
        return False

