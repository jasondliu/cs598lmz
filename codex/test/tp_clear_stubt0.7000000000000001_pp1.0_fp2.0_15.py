import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

def test():
    f = func
    del func
    f()

for i in xrange(50):
    test()
class CustomException(Exception):
    def __init__(self):
        self.args = (self,)
        self.x = 1

class X:
    def __del__(self):
        raise CustomException()

