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

def fin():
    latefin.ref = weakref.ref(func)
    del latefin

def f():
    global func
    func = fin

f()

if __name__ == '__main__':
    import gc
    gc.collect()
    import time
    time.sleep(0.1)
    from test.test_weakref import run_unittest
    run_unittest(WeakNamespaceTest)
