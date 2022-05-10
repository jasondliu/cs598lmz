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
del func, cyc, LateFin

gc.enable()

# create a following chain:
#   func <-> cyc <-> latefin <-> func
# where only func has a finalizer
#
# For test_cyclic_finalization_order to check that the order is:
#   func, cyc, latefin
a = []
class C:
    def __del__(self):
        a.append(self)
        b = [None] * 100000

c = C()
c.__dict__['d'] = c

del c
