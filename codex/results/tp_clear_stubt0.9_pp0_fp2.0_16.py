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

def mc9(L):
    """
    >>> mc9([99, 88, 77, 66, 55, 44, 33, 22, 11])
    [11, 22, 33, 44, 55, 66, 77, 88, 99]

    """
    for x in range(0, len(L)):
        for y in range(x, len(L)):
            if L[y] < L[x]:
                temp 
