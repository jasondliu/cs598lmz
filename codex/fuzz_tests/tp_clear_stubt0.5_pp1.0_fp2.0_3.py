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
gc.collect()
gc.collect()

"""

def test_weakref_with_callback_and_finalizer_on_cycle():
    import gc, weakref
    import sys

    class Callback:
        def __del__(self):
            global func
            func = self.ref()

    class Finalizer:
        def __del__(self):
            global latefin
            del latefin

    latefin = Finalizer()
    func = lambda: None
    cyc = tuple.__new__(Cyclic, (func, latefin))

    func.__module__ = cyc
    del func, cyc

    r = weakref.ref(cyc[0], lambda x: cyc[1].ref(x))
    del cyc

    gc.collect()
    gc.collect()
    gc.collect()

    assert r() is None

def test_weakref_with_callback_on_cycle():
    import gc, weakref

    class Callback:
        def __del__(self
