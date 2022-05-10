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


class weakSubclass(weakref.ref): pass
class cyclicWeakSubclass(weakref.ref):
    pass
class weakBuiltin: pass
class cyclicWeakBuiltin: pass
class weakReference: pass
class cyclicWeakReference:
    pass
class weakSubclass(weakref.ref): pass


def _func():
    return 1

o_weak = weakSubclass(_func, print)
del _func
gc.collect()

def _func1():
    return 2
def _func2():
    return 3
a_cyclic_weak = cyclicWeakSubclass(_func1, _func2)

def _func3():
    return 4
def _func4():
    return 5
b_cyclic_weak = cyclicWeakBuiltin(_func3, _func4)

def _func5():
    return 6
def _func6():
    return 7
c_cyclic_weak = cyclicWeakReference(_func5, _func6)

a_weak = weakBuiltin(_func2, _func1)
