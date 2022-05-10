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
gc.collect()    # func is live because it's a global in m.  cyc is
                # live because of its ref from l.
del latefin
func = None
gc.collect()    # func is dead because its ref from l died.  m is dead
                # because its ref from func died.  l is live because it's
                # a global.  cyc is dead because func died.
