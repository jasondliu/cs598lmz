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


for i in range(2):
    gc.enable()
    gc.collect()
    gc.collect()
    gc.disable()
    latefin.ref = weakref.ref(func)
    import sys
    # Clear the module cache to forget our old fin
    sys.modules.pop('__main__', None)
    del sys
    gc.collect()
    if not latefin.ref:
        raise AssertionError('Did not run __del__ on cycle')
    func()
    if not latefin.ref:
        raise AssertionError('Ran __del__ twice on cycle')
    gc.enable()
    gc.collect()
    gc.collect()
    gc.disable()
    func()
