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
del func, cyc, LateFin, Cyclic, gc.collect
del weakref, gc



def main(n, *args):
    for i in range(n):
        try:
            f(*args)
        except TypeError:
            pass

def test(n, *args):
    t0 = time.perf_counter()
    main(n, *args)
    t1 = time.perf_counter()
    return t1 - t0

if __name__ == '__main__':
    print(test(100, 1))
